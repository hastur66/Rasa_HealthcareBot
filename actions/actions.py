from typing import Any, Text, Dict, List, Union

from rasa_sdk.events import SlotSet

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher

class AppoinmentForm(FormAction):
    def name(self) -> Text:
        return "appointment_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["patient_name", "telephone", "appointment_date", "pressure"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "patient_name": [self.from_text()],
            "telephone": [self.from_text()],
            "appointment_date": [self.from_text()],
            "pressure": [self.from_entity("pressure")]
        }
    
    @staticmethod
    def validate_appointment_date(
            value, dispatcher, tracker, domain
    ) -> Dict[Text, Any]:
        if value == 'today':
            return {"appointment_date": value}
        else:
            dispatcher.utter_message(text = "Invalid date")
            return {"appointment_date": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(text = "Form is complete")
        return [SlotSet('patient_name', None), SlotSet('telephone', None), SlotSet('appointment_date', None), SlotSet('pressure', None)]

# custom action search
class ActionHospitalSearch(Action):
    def name(self) -> Text:
        return "action_hospital_search"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        #logic
        dispatcher.utter_message(template = 'utter_action_hospital_search')
        return []