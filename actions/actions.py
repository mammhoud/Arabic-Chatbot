# This files contains your custom actions which can be used to run
# custom Python code.
# https://rasa.com/docs/rasa/custom-actions

import json
import re
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormValidationAction
from rasa.core.services import EventStore

async def get_previous_user_message(self, sender_id: str) -> str:
    previous_messages = await self.event_store.get_events(
        "user", sender_id, event_type="user"
    )
    if previous_messages:
        return previous_messages[-1].get("text")

    return None
class SubmitReviewForm(FormValidationAction):
    def name(self) -> str:
        return "submit_review_form"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: "DomainDict") -> list:
        name = tracker.get_slot("name")
        rating = tracker.get_slot("rating")
        review = tracker.get_slot("review")

        if name is not None and rating is not None and review is not None:
            review_text = f"Name: {name}, Rating: {rating}, Review: {review}"
            return [SlotSet("name", None), SlotSet("rating", None), SlotSet("review", None), SlotSet("user_reviews", review_text)]
        else:
            dispatcher.utter_message(text="عفوا لوجود بعض الاخطاء الان يمكنك ارسال رايك فى اي وقت و سيتم التجاوب معك منا!.")
            return []


class ActionBankingCardActivated(Action):
    def name(self) -> Text:
        return "action_banking_card_activated"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        card_number = next(tracker.get_latest_entity_values("card_number"), None)
        #pattern = re.compile("^(5[1-5][0-9]{14}|2(22[1-9][0-9]{12}|2[3-9][0-9]{13}|[3-6][0-9]{14}|7[0-1][0-9]{13}|720[0-9]{12}))$")
        #if pattern.match(card_number):
        dispatcher.utter_message(text="تم التاكد من اشتراكك شكرا لك على ثقتكم")
        
        #else:
        #    dispatcher.utter_message(text="Invalid number!")
        return []


class ValidateReviewForm(FormValidationAction):
    def name(self):
        return "validate_review_form"

    async def run(self, dispatcher, tracker, domain):
        if tracker.get_slot("rating") == "low":
            return {"rating": 1}
        elif tracker.get_slot("rating") == "medium":
            return {"rating": 3}
        elif tracker.get_slot("rating") == "high":
            return {"rating": 5}

class SubmitReviewForm(Action):
    def name(self):
        return "submit_review_form"

    async def run(self, dispatcher, tracker, domain):
        # Here you can implement your logic to save the form data
        # For example, you can call an API or save the data in a database
        dispatcher.utter_message(text="Thank you for your review!")
        return []
# class SendMessageToTelegramUser(Action):

    # def name(self):
        # return "action_send_message_to_telegram_user"

    # def run(self, dispatcher, tracker, domain):
        # user_id = tracker.get_slot("user_id")

        # dispatcher.utter_message(
            # text="Hello!", to=user_id
        # )
#         # return []
# class ActionBankingExchangeRate(Action):
#     def name(self) -> Text:
#         return "action_exchange_rate"
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         url = "https://api.apilayer.com/exchangerates_data/"

#         payload = {}
#         headers= {
#         "apikey": "NKd5K7kfckOVRG3KdMWNk8Q1hj0E7bID"
#         }
#         response = requests.request("GET", url, headers=headers, data = payload)
#         responseJSON = response.json();
#         status_code = response.status_code
#         dispatcher.utter_message(text=str(responseJSON['result']));
#         return []
