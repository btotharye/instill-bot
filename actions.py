from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import json

with open('drinks.json', 'r') as f:
    drink_recipes_dict = json.load(f)

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

        print(f"The drink value to validate is: {value.lower()}")

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

        for drink_recipe in drink_recipes_dict:
            if drink_recipe['name'] == drink:
                print(f"The drink recipe is: {drink_recipe}")

        # utter submit template
        dispatcher.utter_message(template="utter_submit")
        return []
