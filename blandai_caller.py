#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: kaiyrbekovk2
"""

import requests
import os
from dotenv import load_dotenv
import json 
from datetime import datetime

load_dotenv()
API_KEY = os.getenv('BLANDAI_API_KEY')
PHONE_NUMBER = os.getenv("PHONE_NUMBER")


def send_call(task_prompt, phone_number, conversational_model = "base"):
    url = "https://api.bland.ai/v1/calls"
    payload = {
        "phone_number": PHONE_NUMBER,
        "task": task_prompt,
        "voice": "Allie",
        "wait_for_greeting": True,
        "block_interruptions": True,
        "interruption_threshold": 123,
        "model": conversational_model,
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


    response = requests.request("POST", url, json=payload, headers=headers, verify=False)
    call_id = json.loads(response.text)["call_id"]
    return call_id


def retrieve_and_save_transcripts(participant_id, call_ids, blandai_data_dir = './blandai-data'):
    headers = {
        "authorization": API_KEY,
    }
    transcripts = {}
    for i in range(len(call_ids)):
        call_id = call_ids[i]
        url = f"https://api.bland.ai/v1/calls/{call_id}"
        response = requests.request("GET", url, headers=headers, verify=False) #
        response_dict = json.loads(response.text)
    
        #print(response_dict["concatenated_transcript"])
        transcripts[i] = response_dict["concatenated_transcript"]
    
    fname  = os.path.join(blandai_data_dir,  f"participant{participant_id}_blandai_transcripts_{datetime.today().strftime('%Y-%m-%d')}.json")
    with open(fname, "w") as f:
        f.write(json.dumps(transcripts)) 
    return fname
        
        
        
#retrieve_and_save_transcripts(1, "a")