## happy path w/greet
* greet
    - utter_greet
* request_drink_recipe
    - drink_form
    - form{"name": "drink_form"}
    - form{"name": null}
* thanks
    - utter_thanks
* goodbye
    - action_goodbye
    - action_cancel

## happy path no greet
* request_drink_recipe
    - drink_form
    - form{"name": "drink_form"}
    - form{"name": null}
    - action_cancel

## ask about drink recipe list
* drink_list
    - action_drink_list
    - action_cancel

## say goodbye
* goodbye
  - action_cancel

## bot challenge
* bot_challenge
  - utter_iamabot
  - action_cancel

## rum punch story
* greet
    - utter_greet
* request_drink_recipe{"drink":"rum punch"}
    - drink_form
    - form{"name":"drink_form"}
    - slot{"drink":"rum punch"}
    - form{"name":null}
    - slot{"requested_slot":null}
* thanks
    - utter_thanks
    - action_cancel

## hemingway story
* request_drink_recipe{"drink":"hemingway"}
    - drink_form
    - form{"name":"drink_form"}
    - slot{"drink":"hemingway"}
    - form{"name":null}
    - slot{"requested_slot":null}
* thanks
    - utter_thanks
    - action_cancel

## help Story
* help
    - utter_help

## ask hours
* hours
    - utter_hours
    - action_cancel


## food options
* food
    - utter_food
* thanks
    - utter_thanks
    - action_cancel

## greet with food question
* greet
    - utter_greet
* food
    - utter_food
* thanks
    - utter_thanks
    - action_cancel

## Story from conversation with 98f143c1-704f-471c-a5fd-03e5cc067297 on January 25th 2020
* greet
    - utter_greet
* hours
    - utter_hours
* food
    - utter_food
    - action_cancel

## greet with bot challenge and pet friendly
* greet
    - utter_greet
* bot_challenge
    - utter_iamabot
    - action_cancel

## tours story
* tours
    - utter_tours
    - action_cancel

## pet friendly story
* pet_friendly
    - utter_petfriendly
    - action_cancel

## greet with bot challenge
* greet
    - utter_greet
* bot_challenge
    - utter_iamabot

## thanks
* thanks
    - utter_thanks
    - action_cancel