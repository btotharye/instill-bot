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
    - utter_goodbye

## happy path no greet
* request_drink_recipe
    - drink_form
    - form{"name": "drink_form"}
    - form{"name": null}

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

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

## hemingway story
* request_drink_recipe{"drink":"hemingway"}
    - drink_form
    - form{"name":"drink_form"}
    - slot{"drink":"hemingway"}
    - form{"name":null}
    - slot{"requested_slot":null}
* thanks
    - utter_thanks

## help Story
* help
    - utter_help

## ask hours
* hours
    - utter_hours

## food options
* food
    - utter_food
* thanks
    - utter_thanks

## greet with food question
* greet
    - utter_greet
* food
    - utter_food
* thanks
    - utter_thanks

## Story from conversation with 98f143c1-704f-471c-a5fd-03e5cc067297 on January 25th 2020
* greet
    - utter_greet
* hours
    - utter_hours
* food
    - utter_food

## greet with bot challenge and pet friendly
* greet
    - utter_greet
* bot_challenge
    - utter_iamabot
    
## tours story
* tours
    - utter_tours

## pet friendly story
* pet_friendly
    - utter_petfriendly
