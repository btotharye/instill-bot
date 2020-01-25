## drink recipe list
* drink_list: what recipes do you know?
    - action

## Happy path drink recipe
* request_drink_recipe: im looking for a drink recipe
    - drink_form
    - form{"name": "drink_form"}
    - form{"name": null}

## hemingway story test
* request_drink_recipe: I want to make a [hemingway](drink)
    - drink_form
    - form{"name":"drink_form"}
    - slot{"drink":"hemingway"}
    - form{"name":null}
    - slot{"requested_slot":null}
* thanks: thanks
    - utter_thanks

## rum punch story test
* request_drink_recipe: I want to make a [Rum Punch](drink)
    - drink_form
    - form{"name":"drink_form"}
    - slot{"drink":"rum punch"}
    - form{"name":null}
    - slot{"requested_slot":null}
* thanks: thanks
    - utter_thanks

## hello then ask about hours
* greet: hello
    - utter_greet
* hours: when are you open?
    - utter_hours

## ask hours story test
* hours: what are your hours?
    - utter_hours

## ask about food options test
* food: do you have any food options?
    - utter_food

## ask about pet friendly test
* pet_friendly: are dogs allowed?
    - utter_petfriendly