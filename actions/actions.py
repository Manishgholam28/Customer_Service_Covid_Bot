# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import datetime as dt

class ActionDateTime(Action):

    def name(self) -> Text:
        return "action_date_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        now = dt.datetime.now()
        dispatcher.utter_message(text=str(now))

        return []
        
class ActionCoronaInfo(Action):

    def name(self) -> Text:
        return "action_corona_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        now = 'Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus. More info at:'+'https://www.hopkinsmedicine.org/health/conditions-and-diseases/coronavirus'
        dispatcher.utter_message(text=str(now))

        return []
        
class ActionCoronaSpread(Action):

    def name(self) -> Text:
        return "action_corona_spread"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        now = 'The disease can spread from person to person through small droplets from the nose or mouth which are spread when a person with COVID-19 coughs or exhales. These droplets land on objects and surfaces around the person. More info at: '+'https://www.webmd.com/lung/coronavirus-transmission-overview#1'
        dispatcher.utter_message(text=str(now))

        return []

class ActionCoronaHarm(Action):

    def name(self) -> Text:
        return "action_corona_harm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        now = 'It is a virus which is never seen amog humans so we are not immune to it, which makes it harmful. More info: '+'https://www.webmd.com/lung/coronavirus-covid-19-affects-body#1'
        dispatcher.utter_message(text=str(now))

        return []
        
class ActionCoronaStop(Action):

    def name(self) -> Text:
        return "action_corona_stop"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        now = 'It can be stoped from spreading by taking various preventive measures. More info: '+'https://www.health.harvard.edu/diseases-and-conditions/preventing-the-spread-of-the-coronavirus'
        dispatcher.utter_message(text=str(now))

        return []

class ActionCoronaVaccine(Action):

    def name(self) -> Text:
        return "action_corona_vaccine"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        now = 'Vaccine has become more available for everyone. Here are some centers around you: '+'https://www.google.com/search?q=corona+vaccine+centre+near+me&sxsrf=AOaemvItwwuD5SUFKLEYjt_2A591B5zoCg%3A1635536840659&source=hp&ei=yE98YcH0JM6a4t4PxO6xsAI&iflsig=ALs-wAMAAAAAYXxd2EYfXNfaIHvgzLc2xhwqSEpCS6kM&oq=corona+vaccine+cen&gs_lcp=Cgdnd3Mtd2l6EAEYADIICAAQgAQQyQMyBQgAEJIDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6DQguEMcBEK8BECcQkwI6BAgjECc6BwgAELEDEEM6BAgAEEM6CggAELEDEIMBEEM6DQgAELEDEIMBEMkDEEM6DQguEMcBENEDEEMQkwI6BggAEAoQQzoKCAAQsQMQgwEQCjoHCAAQgAQQCjoECAAQCjoHCC4QgAQQCjoFCAAQkQI6CwgAEIAEELEDEIMBOg4IABCABBCxAxCDARDJAzoICAAQsQMQgwE6CAgAELEDEJECOgsIABCxAxDJAxCRAjoKCAAQgAQQsQMQCjoICAAQgAQQsQM6DQgAEIAEELEDEIMBEApQow1Y2kJg2FVoAXAAeACAAZEBiAHNEZIBBDAuMTmYAQCgAQE&sclient=gws-wiz'
        dispatcher.utter_message(text=str(now))

        return []