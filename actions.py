# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# coding=utf-8
import logging
from datetime import datetime
from typing import Any, Text, Dict, List
import json

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, UserUtteranceReverted, ConversationPaused
import psycopg2
import requests

logger = logging.getLogger('test')
logging.basicConfig()
logger.setLevel(logging.DEBUG)
# logger.info('I am <info> message.')
# logger.debug('I am <debug> message.')

class DBUtil():


    @staticmethod
    def query(str_query):
        conn = psycopg2.connect(database="test", user="postgres", password="nick", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        cur.execute(str_query)

        # 获取结果集的每一行
        rows = cur.fetchall()
        conn.close()
        return rows

class CheckVisaForm(FormAction):
    content = ""
    url = ""
    slots = ["nationality"]
    slot_nationality = "nationality"
    slot_visa_purpose = "visa_purpose"
    slot_check_visa_tourism_family = "check_visa_tourism_family"
    slot_check_visa_tourism_valid_article = "check_visa_tourism_valid_article"
    slot_check_visa_work = "check_visa_work"
    slot_check_visa_study = "check_visa_study"
    slot_check_visa_family_valid_article = "check_visa_family_valid_article"
    slot_check_visa_family_UK = "check_visa_family_UK"
    slot_check_visa_family_EEA = "check_visa_family_EEA"

    total_slots = [slot_nationality, slot_visa_purpose, slot_check_visa_tourism_family, slot_check_visa_tourism_valid_article,
                   slot_check_visa_work, slot_check_visa_study, slot_check_visa_family_valid_article, slot_check_visa_family_UK,
                   slot_check_visa_family_EEA]

    def name(self):
        return "check_visa_form"

    @staticmethod
    def required_slots(tracker):
        logger.debug('-------------------I am <debug> message.')
        CheckVisaForm.get_slots(tracker)
        return CheckVisaForm.slots

    # @staticmethod
    # def required_slots(tracker: Tracker) -> List[Text]:
    #     """A list of required slots that the form has to fill"""
    #     return ["country", "visa_purpose"]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        str=""
        if CheckVisaForm.content:
            str = CheckVisaForm.content + "\n"
        if CheckVisaForm.url:
            str += "Please check following URL for details:\n" + CheckVisaForm.url
        dispatcher.utter_message(str)
        CheckVisaForm.slots = ["nationality"]
        reset_slots = CheckVisaForm.get_reset_total_slots(tracker)
        return reset_slots

    @staticmethod
    def get_reset_total_slots(tracker):
        logger.info('+++++++++++++++++++++++++++<reset_total_slots> +++++++++++++++++++++++++++.' )
        reset_slots = []
        for slot in CheckVisaForm.total_slots:
            logger.info('+++++++++++++++++++++++++++<total_slots> +++++++++++++++++++++++++++.' + slot)
            if tracker.get_slot(slot):
                reset_slots.append(SlotSet(slot, None))
        return reset_slots
        logger.info('+++++++++++++++++++++++++++<nationality> +++++++++++++++++++++++++++.')

    @staticmethod
    def get_slots(tracker):
        if tracker.get_slot("nationality"):
            rows_check_visa_one = CheckVisaForm.check_visa_one(tracker.get_slot("nationality"))
            if len(rows_check_visa_one) == 1:
                CheckVisaForm.set_result(rows_check_visa_one[0][1], rows_check_visa_one[0][2])
            else:
                visa_purpose = tracker.get_slot("visa_purpose")
                if not visa_purpose:
                    CheckVisaForm.add_slot(CheckVisaForm.slot_visa_purpose)
                else:
                    if visa_purpose != "Transit":
                        rows_check_visa_not_transit = CheckVisaForm.check_visa_not_transit(tracker)
                        end, slot = CheckVisaForm.check_whether_end_not_transit(tracker, rows_check_visa_not_transit)
                        if end:
                            CheckVisaForm.set_result(rows_check_visa_not_transit[0][9],
                                                     rows_check_visa_not_transit[0][10])
                        else:
                            CheckVisaForm.add_slot(slot)
                    # else:






    @staticmethod
    def add_slot(slot):
        if slot not in CheckVisaForm.slots:
            CheckVisaForm.slots.append(slot)

    @staticmethod
    def check_visa_one(value_nationality):
        str_query = "SELECT * FROM \"Check_visa_one\" where LOWER(nationality) =" + "LOWER(\'"+value_nationality+ "\')"
        rows = DBUtil.query(str_query)
        return rows

    @staticmethod
    def check_visa_not_transit(tracker):
        query_conditions = ""
        if tracker.get_slot("nationality"):
            query_conditions = "LOWER(nationality) =" + "LOWER(\'"+tracker.get_slot("nationality")+ "\')"
        if tracker.get_slot("visa_purpose"):
            query_conditions += "AND LOWER(\"visa_purpose\") =" + "LOWER(\'"+tracker.get_slot("visa_purpose")+ "\')"
        if tracker.get_slot("check_visa_tourism_family"):
            query_conditions += "AND LOWER(\"check_visa_tourism_family\") =" + "LOWER(\'"+tracker.get_slot("check_visa_tourism_family")+ "\')"
        if tracker.get_slot("check_visa_tourism_valid_article"):
            query_conditions += "AND LOWER(\"check_visa_tourism_valid_article\") =" + "LOWER(\'"+tracker.get_slot("check_visa_tourism_valid_article")+ "\')"
        if tracker.get_slot("check_visa_work"):
            query_conditions += "AND LOWER(\"check_visa_work\") =" + "LOWER(\'"+tracker.get_slot("check_visa_work")+ "\')"
        if tracker.get_slot("check_visa_study"):
            query_conditions += "AND LOWER(\"check_visa_study\") =" + "LOWER(\'"+tracker.get_slot("check_visa_study")+ "\')"
        if tracker.get_slot("check_visa_family_valid_article"):
            query_conditions += "AND LOWER(\"check_visa_family_valid_article\") =" + "LOWER(\'"+tracker.get_slot("check_visa_family_valid_article")+ "\')"
        if tracker.get_slot("check_visa_family_UK"):
            query_conditions += "AND LOWER(\"check_visa_family_UK\") =" + "LOWER(\'"+tracker.get_slot("check_visa_family_UK")+ "\')"
        if tracker.get_slot("check_visa_family_EEA"):
            query_conditions += "AND LOWER(\"check_visa_family_EEA\") =" + "LOWER(\'"+tracker.get_slot("check_visa_family_EEA")+ "\')"

        str_query = "SELECT * FROM \"Check_visa_not_transit\" where " + query_conditions
        rows = DBUtil.query(str_query)
        return rows

    @staticmethod
    def check_whether_end_not_transit(tracker, rows):
        end, slot = True, None
        if (not tracker.get_slot("nationality")) and rows[0][0]:
            end, slot = False, "nationality"
            return end, slot
        if (not tracker.get_slot("visa_purpose")) and rows[0][1]:
            end, slot = False, "visa_purpose"
            return end, slot
        if (not tracker.get_slot("check_visa_tourism_family")) and rows[0][2]:
            end, slot = False, "check_visa_tourism_family"
            return end, slot
        if (not tracker.get_slot("check_visa_tourism_valid_article")) and rows[0][3]:
            end, slot = False, "check_visa_tourism_valid_article"
            return end, slot
        if (not tracker.get_slot("check_visa_work")) and rows[0][4]:
            end, slot = False, "check_visa_work"
            return end, slot
        if (not tracker.get_slot("check_visa_study")) and rows[0][5]:
            end, slot = False, "check_visa_study"
            return end, slot
        if (not tracker.get_slot("check_visa_family_valid_article")) and rows[0][6]:
            end, slot = False, "check_visa_family_valid_article"
            return end, slot
        if (not tracker.get_slot("check_visa_family_UK")) and rows[0][7]:
            end, slot = False, "check_visa_family_UK"
            return end, slot
        if (not tracker.get_slot("check_visa_family_EEA")) and rows[0][8]:
            end, slot = False, "check_visa_family_EEA"
            return end, slot
        return end, slot

    @staticmethod
    def set_result(content, url):
        CheckVisaForm.content = content
        CheckVisaForm.url = url

class ActionTest(Action):
   def name(self) -> Text:
      return "action-test"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       tracker.get_slot("nationality")
       return []

class ActionChitchat(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self):
        return "action_chitchat"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message["intent"].get("name")

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in [
            "ask_builder",
            "ask_weather",
            "ask_howdoing",
            "ask_whatspossible",
            "ask_whatisrasa",
            "ask_isbot",
            "ask_howold",
            "ask_languagesbot",
            "ask_restaurant",
            "ask_time",
            "ask_wherefrom",
            "ask_whoami",
            "ask_whatismyname",
            "ask_howbuilt",
            "ask_whoisit",
        ]:
            dispatcher.utter_template("utter_" + intent, tracker)
        return []

class ActionFetchProfile(Action):
   def name(self) -> Text:
      return "action_fetch_profile"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       return [SlotSet("account_type", "premium")]