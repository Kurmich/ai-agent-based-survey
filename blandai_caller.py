#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 14:39:10 2024

@author: kaiyrbekovk2
"""

import requests
import os
from dotenv import load_dotenv
import json 

load_dotenv()
API_KEY = os.getenv('BLANDAI_API_KEY')
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

print(API_KEY, PHONE_NUMBER)
intro = "Your name is Sarah, and you’re a surveyor for COVID-19 Household Impact Survey. The goal of the survey is to provide national and regional statistics about physical health, mental health, economic security, and social dynamics in the United States.\n" 
  

survey_questions = '''Here are the questions that you need to ask, give enough time to reply, introduce yourself and let them know the purpose of the survey:
                    Generally speaking, would you say that you can trust all the people, most of the people, some of the people, or none of the people in your neighborhood? 
                    In the past month, how often did you talk with any of your neighbors?
                    During a typical month prior to March 1, 2020, when COVID-19 began spreading in the United States, how often did you talk with any of your neighbors?
                    In the past month, how often did you communicate with friends and family by phone, text, email, app, or using the Internet?
                    During a typical month prior to March 1, 2020, when COVID-19 began spreading in the United States, how often did you communicate with friends and family by phone, text, email, app, or using the Internet?
                    In the past month, did you spend any time volunteering for any organization or association, or not?
                    During a typical month prior to March 1, 2020, when COVID-19 began spreading in the United States, did you spend any time volunteering for any organization or association, or not?
                    Would you say your health in general is excellent, very good, good, fair, or poor?
                    [Fever] Have you experienced any of the following symptoms in the past 7 days, or not?
                    [Chills] Have you experienced any of the following symptoms in the past 7 days, or not?'''

       
         
dialogue = '''Here is an example dialogue
            You: Hi, thank you for participating in this survey. Lets get started with the first question. Generally speaking, would you say that you can trust all the people, most of the people, some of the people, or none of the people in your neighborhood? 
            Person: I would say I can trust some of the people in my neighborhood.
            You: Thank you. In the past month, how often did you talk with any of your neighbors?
            Person: In the past month, I talked with my neighbors a few times a week.
            You: And during a typical month prior to March 1, 2020, when COVID-19 began spreading in the United States, how often did you talk with any of your neighbors?  
            Person: Before COVID-19, I used to talk with my neighbors almost daily.  
            You: In the past month, how often did you communicate with friends and family by phone, text, email, app, or using the Internet?  
            Person: I communicated with friends and family every day in the past month.  
            You: During a typical month prior to March 1, 2020, when COVID-19 began spreading in the United States, how often did you communicate with friends and family by phone, text, email, app, or using the Internet?  
            Person: Before COVID-19, I still communicated with friends and family almost every day.  
            You: In the past month, did you spend any time volunteering for any organization or association, or not?  
            Person: No, I did not spend any time volunteering in the past month.  
            You: During a typical month prior to March 1, 2020, when COVID-19 began spreading in the United States, did you spend any time volunteering for any organization or association, or not?  
            Person: Yes, I used to volunteer once a week before COVID-19.  
            You: Lastly, would you say your health in general is excellent, very good, good, fair, or poor?  Person: I would say my health is good.  
            You: Thank you. Now, moving on to the next set of questions. Have you experienced any of the following symptoms in the past 7 days, or not? Let's start with fever.  
            Person: No, I have not experienced a fever in the past 7 days.  You: How about chills? Have you experienced chills in the past 7 days, or not?  
            Person: No, I have not experienced chills in the past 7 days.  
            You: Thank you for your time and for answering these questions. Have a great day!  
            Person: You too, thank you!'''




task = intro + survey_questions + dialogue

task = 'Say Hello. Then hang up.'



print(task)


url = "https://api.bland.ai/v1/calls"

payload = {
    "phone_number": PHONE_NUMBER,
    "task": task,
    "voice": "nat",
    "wait_for_greeting": True,
    "block_interruptions": True,
    "interruption_threshold": 123,
    "model": "base",
    "temperature": 0.7,
    "transfer_list": {},
    "language": "en",
    "timezone": "US/Eastern",
    "retry": {},
    "max_duration": 30,
    "record": True,
    "answered_by_enabled": True
}
headers = {
    "authorization": API_KEY,
}

 #"Content-Type": "application/json"
 
#print(headers)
response = requests.request("POST", url, json=payload, headers=headers)
print(response.text)


'''
call_id =  "0aa7abbd-b5b2-4cb8-b086-88629432548c"#"14230927-454d-471a-909a-9ae9d3cd84b8"
url = f"https://api.bland.ai/v1/calls/{call_id}"

print(url)
response = requests.request("GET", url, headers=headers)
#print(response["transcripts"])
#print(response.text)
response_dict = json.loads(response.text)

print(response_dict["concatenated_transcript"])

'''

'''
call_ids = ["f897a79b-5911-4b23-a6c4-4825f0c35030", "5427acb4-bcee-469c-af78-845ee8c669e3", "6ce13d57-305e-40de-92e7-7e9edd31bf30", "dde1772c-13f1-454c-8bbe-081780616c5d", "2ac2e420-d434-4e74-ae0c-02489bedf7a8", 
            "9524e9ea-2932-43c8-86ad-38aadcb67c28", "9531a44b-1a02-4974-a852-ff721868f8b1", "3ac76823-f561-4c4a-82fe-f853941e820c", "42562149-29e1-4a95-8e5d-a04c57635d7d", "81306b5c-a9a9-4326-b399-b23d5a05a55c"]


transcripts = {}


for i in range(len(call_ids)):
    call_id = call_ids[i]
    url = f"https://api.bland.ai/v1/calls/{call_id}"
    response = requests.request("GET", url, headers=headers)
    response_dict = json.loads(response.text)

    print(response_dict["concatenated_transcript"])
    transcripts[i] = response_dict["concatenated_transcript"]
    

# Write JSON string to a file
with open("transcripts.json", "w") as f:
    f.write(json.dumps(transcripts))
    '''