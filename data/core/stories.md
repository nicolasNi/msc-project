## thanks
* thank
    - utter_noworries
    - utter_anything_else

## bye
* **bye**
    - utter_bye
    
## greet
* greet 
    - utter_greet_noname
    - utter_what_help
> check_greet


## anything else? - yes
    - utter_anything_else
* affirm
    - utter_what_help

## anything else? - no
    - utter_anything_else
* deny
    - utter_thumbsup


## Greet -- Check if you need a UK visa + feedback
> check_greet
* check_visa
    - utter_can_do
    - check_visa_form
    - form{"name": "check_visa_form"}
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_thumbsup
    - utter_anything_else
    
## Greet -- Check if you need a UK visa + affirm feedback
> check_greet
* check_visa
    - utter_can_do
    - check_visa_form
    - form{"name": "check_visa_form"}
    - form{"name": null}
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else
    
## Greet -- Check if you need a UK visa + deny feedback
> check_greet
* check_visa
    - utter_can_do
    - check_visa_form
    - form{"name": "check_visa_form"}
    - form{"name": null}
    - utter_ask_feedback
* deny
    - utter_thumbsup
    - utter_anything_else
    
    
## Check if you need a UK visa + feedback
* check_visa
    - utter_can_do
    - check_visa_form
    - form{"name": "check_visa_form"}
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_thumbsup
    - utter_anything_else
    
## Check if you need a UK visa + affirm feedback
* check_visa
    - utter_can_do
    - check_visa_form
    - form{"name": "check_visa_form"}
    - form{"name": null}
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else
    
## Check if you need a UK visa + deny feedback
* check_visa
    - utter_can_do
    - check_visa_form
    - form{"name": "check_visa_form"}
    - form{"name": null}
    - utter_ask_feedback
* deny
    - utter_thumbsup
    - utter_anything_else
    
## Check if you need a UK visa + feedback -- stop but continue
* check_visa
    - utter_can_do
    - check_visa_form
    - form{"name": "check_visa_form"}
* canthelp OR deny
    - utter_ask_continue_check_visa
* affirm
    - utter_great
    - check_visa_form
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_thumbsup
    - utter_anything_else
    
## Check if you need a UK visa + feedback -- stop multiple times but continue
* check_visa
    - utter_can_do
    - check_visa_form
    - form{"name": "check_visa_form"}
* canthelp OR deny
    - utter_ask_continue_check_visa
* affirm
    - utter_great
    - check_visa_form
* canthelp OR deny
    - utter_ask_continue_check_visa
* affirm
    - utter_great
    - check_visa_form
* canthelp OR deny
    - utter_ask_continue_check_visa
* affirm
    - utter_great
    - check_visa_form
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_thumbsup
    - utter_anything_else
    
## Check if you need a UK visa + feedback -- stop and really stop
* check_visa
    - utter_can_do
    - check_visa_form
    - form{"name": "check_visa_form"}
* canthelp OR deny
    - utter_ask_continue_check_visa
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - utter_anything_else

## Chichat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
> check_chichat

## Greet -- chichat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    
## Check if you need a UK visa + chichat
* check_visa
    - utter_can_do
    - check_visa_form
    - form{"name": "check_visa_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - check_visa_form
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - check_visa_form
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - check_visa_form
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_thumbsup
    - utter_anything_else