# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
#
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []


#class ActionRestaurantSearch(Action):

#    def name(self) -> Text:
#        return "action_restaurant_search"

#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#        entities = tracker.latest_message['entities']
#        print(entities)

#        for e in entities:
#        	if e['entity'] == 'hotel':
#        		name = e['value']

#        	if name == 'Indian':
#        		message = 'Indian1, Indian2, Indian3, Indian4, Indian5'

#        	if name == 'Italian':
#        		message = 'Italian1, Italian2, Italian3, Italian4, Italian5'
#        	if name == 'Thai':
#        		message = 'Thai1, Thai2, Thai3, Thai4, Thai5'

#        dispatcher.utter_message(text=message)

#        return []


class ActionRestaurantSearch(Action):

    def name(self) -> Text:
        return "action_restaurant_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'hotel':
                message = 'Okay...looking for a restaurant at'
               
                           
            
        dispatcher.utter_message(text=message)

        return []




class ActionCoronaTracker(Action):

    def name(self) -> Text:
        return "action_corona_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

       response = requests.get("https://api.covid19india.org/data.json").json()

       entities = tracker.latest_message['entities']
       print("Message", entities)
       state = None

       for i in entities:

           if i['entity'] == 'state':

            state = i['value'] 

           message = "Please check the spelling of a state"        
       
       if state == "India":

        state = "Total"


       for data in response["statewise"]:
           if data["state"] == state.title():
               print(data)
               message = "Active: "+data['active']+ " recovered : "+data['recovered'] + " confirmed: " +data["confirmed"]

      
       
       dispatcher.utter_message(text= message)

       return []
