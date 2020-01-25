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
