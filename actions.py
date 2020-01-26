import logging

from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import (
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    )
import json

logger = logging.getLogger(__name__)

class ActionPause(Action):
    """Pause the conversation"""

    def name(self) -> Text:
        return "action_pause"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        return [ConversationPaused()]

with open("drinks.json", "r") as f:
    drink_recipes_dict = json.load(f)

class ActionDrinkList(Action):
    """Returns the list of drinks we know recipes for"""

    def name(self) -> Text:
        return "action_drink_list"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        drink_list = []

        for drink_recipe in drink_recipes_dict:
            drink_list.append(drink_recipe["name"])

        recipe_response = "\n".join(str(drink) for drink in drink_list)
        dispatcher.utter_message(
            f"I know about the following drink recipes: {recipe_response}"
        )
        return []


class DrinkForm(FormAction):
    """Custom form action for drink search"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "drink_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["drink"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"drink": self.from_entity(entity="drink")}

    @staticmethod
    def drink_db() -> List[Text]:
        """Database of supported drinks"""

        return [
            "rum punch",
            "joco mule",
            "hemingway",
            "painkiller",
        ]

    def validate_drink(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate drink value."""

        if value.lower() in self.drink_db():
            # validation succeeded, set the value of the "drink" slot to value
            return {"drink": value}
        else:
            dispatcher.utter_message(template="utter_wrong_drink")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"drink": None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        drink = tracker.get_slot("drink")
        drink_recipe = {}

        # Ensure drink recipe is in our drink dict and
        # grab its data for the response.
        for drink_recipe in drink_recipes_dict:
            if drink_recipe["name"] == drink:
                drink_ingredients = " \n".join(
                    [str(elem) for elem in drink_recipe["ingredients"]]
                )
                drink_garnish = drink_recipe["garnish"]

                # Utter recipe to user if found in dictionary from json file.
                dispatcher.utter_message(
                    f"To make a {drink}, you will combine the following "
                    f"ingredients: \n {drink_ingredients} \n"
                    f"and garnish with {drink_garnish}"
                )
        return []


class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def __init__(self) -> None:
        import pandas as pd

        self.intent_mappings = pd.read_csv("intent_description_mappings.csv")
        self.intent_mappings.fillna("", inplace=True)
        self.intent_mappings.entities = self.intent_mappings.entities.map(
            lambda entities: {e.strip() for e in entities.split(",")}
        )

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        intent_ranking = tracker.latest_message.get("intent_ranking", [])
        if len(intent_ranking) > 1:
            diff_intent_confidence = intent_ranking[0].get(
                "confidence"
            ) - intent_ranking[1].get("confidence")
            if diff_intent_confidence < 0.2:
                intent_ranking = intent_ranking[:2]
            else:
                intent_ranking = intent_ranking[:1]
        first_intent_names = [
            intent.get("name", "")
            for intent in intent_ranking
            if intent.get("name", "") != "out_of_scope"
        ]

        message_title = (
            "Sorry, I'm not sure that I've understood " "you correctly 🤔 Do you mean..."
        )

        entities = tracker.latest_message.get("entities", [])
        entities = {e["entity"]: e["value"] for e in entities}

        entities_json = json.dumps(entities)

        buttons = []
        for intent in first_intent_names:
            logger.debug(intent)
            logger.debug(entities)
            buttons.append(
                {
                    "title": self.get_button_title(intent, entities),
                    "payload": "/{}{}".format(intent, entities_json),
                }
            )

        # /out_of_scope is a retrieval intent
        # you cannot send rasa the '/out_of_scope' intent
        # instead, you can send one of the sentences that it will map onto the response
        buttons.append(
            {
                "title": "Something else",
                "payload": "I am asking you an out of scope question",
            }
        )

        dispatcher.utter_button_message(message_title, buttons=buttons)

        return []

    def get_button_title(self, intent: Text, entities: Dict[Text, Text]) -> Text:
        default_utterance_query = self.intent_mappings.intent == intent
        utterance_query = (self.intent_mappings.entities == entities.keys()) & (
            default_utterance_query
        )

        utterances = self.intent_mappings[utterance_query].button.tolist()

        if len(utterances) > 0:
            button_title = utterances[0]
        else:
            utterances = self.intent_mappings[default_utterance_query].button.tolist()
            button_title = utterances[0] if len(utterances) > 0 else intent

        return button_title.format(**entities)


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        # Fallback caused by TwoStageFallbackPolicy
        if (
            len(tracker.events) >= 4
            and tracker.events[-4].get("name") == "action_default_ask_affirmation"
        ):

            dispatcher.utter_template("utter_restart_with_button", tracker)

            return []

        # Fallback caused by Core
        else:
            dispatcher.utter_template("utter_default", tracker)
            return [UserUtteranceReverted()]