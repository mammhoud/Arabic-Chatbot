from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet




class ActionLogin(Action):
    def name(self) -> Text:
        return "action_login"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        username = tracker.get_slot('username')
        passcode = tracker.get_slot('passcode')

        if not username or not passcode:
            # Prompt for username and passcode
            return [SlotSet("is_logged_in", False)]

        # Replace with your actual login logic
        login_successful = login_logic(username, passcode)

        if login_successful:
            # Replace with your actual data signing function
            signed_data = sign_data(username, passcode)
            return [SlotSet("is_logged_in", True), SlotSet("signed_data", signed_data)]

        else:
            dispatcher.utter_message(text="Login failed. Please try again.")
            return [SlotSet("is_logged_in", False)]