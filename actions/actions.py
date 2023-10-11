# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import json
import re
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests



# class ActionCheckLang(Action):
    # def name(self) -> Text:
        # return "action_check_lang"
    # def run(self, dispatcher: CollectingDispatcher,
            # tracker: Tracker,
            # domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
            
        # # to-Do : create which language api
        # selected_lag = next(tracker.get_latest_entity_values("selected_lag"),None)
        # url = "https://api.apilayer.com/exchangerates_data/"
        
        # # change config files nlu language with the selected_lag if lang is ar or en
        # # this action for user language or unknown language to the bot
        # # translate the user input to the common file language if the user input is not arabic or english
        # # first check the user input language, if the language is = ar, en make the nlu file path= the {language_folder} path
        # # then if the language is not handled into nlu file make translation api cached to make new language translation with the nlu default input
        # # considering the best fitting language to train the models (arabic, english) with our fanctions
        # # create new data base with languages
      
        # dispatcher.utter_message(text= f"selected_lag = "{selected_lag}")
class ActionBankingCardActivated(Action):
    def name(self) -> Text:
        return "action_banking_card_activated"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        card_number = next(tracker.get_latest_entity_values("card_number"), None)
        #pattern = re.compile("^(5[1-5][0-9]{14}|2(22[1-9][0-9]{12}|2[3-9][0-9]{13}|[3-6][0-9]{14}|7[0-1][0-9]{13}|720[0-9]{12}))$")
        #if pattern.match(card_number):
        dispatcher.utter_message(text="تم تفعيل البطاقة")
        
        #else:
        #    dispatcher.utter_message(text="Invalid number!")
        return []


# class SendMessageToTelegramUser(Action):

    # def name(self):
        # return "action_send_message_to_telegram_user"

    # def run(self, dispatcher, tracker, domain):
        # user_id = tracker.get_slot("user_id")

        # dispatcher.utter_message(
            # text="Hello!", to=user_id
        # )
        # return []
class ActionBankingExchangeRate(Action):
    def name(self) -> Text:
        return "action_exchange_rate"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = "https://api.apilayer.com/exchangerates_data/"

        payload = {}
        headers= {
        "apikey": "NKd5K7kfckOVRG3KdMWNk8Q1hj0E7bID"
        }
        response = requests.request("GET", url, headers=headers, data = payload)
        responseJSON = response.json();
        status_code = response.status_code
        dispatcher.utter_message(text=str(responseJSON['result']));
        return []
