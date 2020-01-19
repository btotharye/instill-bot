## happy path no greet
* request_drink_recipe
    - action_search_drinks
    - form{"name": "drink_form"}
    - form{"name": null}
    - utter_slots_values

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
