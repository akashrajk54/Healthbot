# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from database_connectivity import DataUpdate,UpdateFeedback
from rasa_sdk.forms import FormAction
from lov import akash
from flu_conform import flu_adult_or_children,flu_treatment,flu_treatment_cost,health_insurance_plan_flu
from laryngitis_conform import laryngitis_adult_or_children,laryngitis_treatment,laryngitis_treatment_cost,health_insurance_plan_laryngitis
#
#
class ActionDatabaseUpdate(Action):
#
    def name(self) -> Text:
        return "action_database_update"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
        name = tracker.get_slot("fname")
        title = tracker.get_slot("lname")
        agee = tracker.get_slot("age")
        symptoms = tracker.get_slot("symp")
        location = tracker.get_slot("location")
        disease = "Fever"

        #dispatcher.utter_message("Outputs are {} {} {} {}:{}".format(name,title,agee,symptoms,disease))
        DataUpdate(tracker.get_slot("fname"),tracker.get_slot("lname"),tracker.get_slot("location"))
        #dispatcher.utter_message("Thanks for your valuable feedback.")
        #dispatcher.utter_message(akash(psymptoms = ['Passing much less urine','Bleeding from any body part','Feeling extremely lethargic/weak']))

        return [SlotSet("disease",disease)]

class ActionDiseaseCoughFever(Action):

    def name(self) -> Text:
        return "action_disease_cough_fever"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("On the basis of your given symptoms, you'r disease type is Cough Fever.")

        return[]

class ActionFeedbackSubmit(Action):

    def name(self) -> Text:
        return "action_feedback_submit"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_feedback_submit")
        #dispatcher.utter_message("Thanks for your valuable feedback.")

        return[SlotSet("feedback", tracker.latest_message['text'])]

class Feedback_into_Database(Action):

    def name(self) -> Text:
        return "action_feedback_database"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Thanks for your valuable feedback.")
        name = tracker.get_slot("fname")
        title = tracker.get_slot("lname")
        feedback = tracker.get_slot("feedback")

        UpdateFeedback(name,title,feedback)
        dispatcher.utter_message("Your feedback is saved to our database. Thank you")


        return[]



class ActionShowSymptomFluBasisOfAge(Action):

    def name(self) -> Text:
        return "action_show_symptom_of_flu_basis_of_age"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        agee = int(tracker.get_slot("age"))

        dispatcher.utter_message(flu_adult_or_children(agee))

        return[]


class ActionDiseaseFluConform(Action):

    def name(self) -> Text:
        return "action_disease_flu_conform"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        agee = int(tracker.get_slot("age"))
        disease = "flu"
        location = tracker.get_slot("location")

        dispatcher.utter_message("On the basis of your given symptoms, you'r disease type is Flu.")
        dispatcher.utter_message("Treatment of your disease is given below:")
        dispatcher.utter_message(flu_treatment(agee))
        dispatcher.utter_message("your treatment cost is:")
        dispatcher.utter_message(flu_treatment_cost(agee))
        dispatcher.utter_message("We are suggesting you the health insurance plan on the basis of oyour location and disease type is:")
        dispatcher.utter_message(health_insurance_plan_flu(location))
        return[]


class ActionShowSymptomLaryngitisBasisOfAge(Action):

    def name(self) -> Text:
        return "action_show_symptom_of_laryngitis_basis_of_age"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        agee = int(tracker.get_slot("age"))

        dispatcher.utter_message(laryngitis_adult_or_children(agee))

        return[]


class ActionDiseaseLaryngitisConform(Action):

    def name(self) -> Text:
        return "action_disease_laryngitis_conform"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        agee = int(tracker.get_slot("age"))
        disease = "laryngitis"
        location = tracker.get_slot("location")

        dispatcher.utter_message("On the basis of your given symptoms, you'r disease type is Laryngitis.")
        dispatcher.utter_message("Treatment of your disease is given below:")
        dispatcher.utter_message(laryngitis_treatment(agee))
        dispatcher.utter_message("your treatment cost is:")
        dispatcher.utter_message(laryngitis_treatment_cost(agee))
        dispatcher.utter_message("We are suggesting you the health insurance plan on the basis of oyour location and disease type is:")
        dispatcher.utter_message(health_insurance_plan_laryngitis(location))

        return[]




































class ActionDiseaseCoughFever(Action):

    def name(self) -> Text:
        return "action_disease_fever_dengu"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("On the basis of your given symptoms, you'r disease type is Fever Dengu.")

        return[]




class ActionDiseaseFeverMeningitis(Action):

    def name(self) -> Text:
        return "action_disease_fever_meningitis"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("On the basis of your given symptoms, you'r disease type is Fever Meningitis.")

        return[]


class ActionDiseaseFeverPharyngitis(Action):

    def name(self) -> Text:
        return "action_disease_fever_pharyngitis"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("On the basis of your given symptoms, you'r disease type is Fever Pharyngitis.")

        return[]


















