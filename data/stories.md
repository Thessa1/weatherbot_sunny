## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
* goodbye
  - utter_goodbye

## happy weather
* greet
  - utter_greet
* weather
  - utter_city
* city
  - action_weather_api
* goodbye
  - utter_goodbye

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
* goodbye
  - utter_goodbye

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* your_name
  - utter_botname
* bot_challenge
  - utter_iamabot
* goodbye
  - utter_goodbye

## New Story

* greet
    - utter_greet
* weather
    - utter_city
* city
    - action_weather_api
* goodbye
    - utter_goodbye

## name
* greet
    - utter_greet
* my_name_is
    - utter_its_nice_to_meet_you
    - utter_assist
* weather
    - utter_city
* city
    - action_weather_api
