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

## Faq ask help
* faq: what can you do
    - respond_faq

## Faq ask hours
* faq: when is instill open
    - respond_faq