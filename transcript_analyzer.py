#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Kurmanbek
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import json
import pandas as pd
from datetime import datetime
from collections import Counter
from pydantic import BaseModel
from typing import Literal
load_dotenv()



client = AzureOpenAI(
  api_key = os.getenv('OPENAI_API_KEY'),  
  api_version = os.getenv('OPENAI_API_VERSION'),
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
)





def get_QA_and_codebook(codebook_file):
    qa_list = []
    with open(codebook_file, 'r') as file:
        codebook = json.load(file)
        question_count = 1
        for code, content in codebook.items():  
            question = content['question']
            qa_list.append(f"Question {question_count}: {question}\nResponse Options: ")
            ans_list = []
            for ans, ans_id in content['clean_response_text_to_id'].items():
                ans_list.append(f"{ans}")
                
            qa_list.append('; '.join(ans_list))
            qa_list.append("\n")
            question_count += 1
    return ''.join(qa_list), codebook


#Define survey responses class with expected format
class SurveyResponses(BaseModel):  
    # Responses for questions 1-4  
    response_to_question_1: Literal[  
        "18-24",   
        "25-34",   
        "35-44",   
        "45-54",   
        "55-64",   
        "65-74",   
        "75+",   
        "Under 18",   
        "OTHER"  
    ]  
    response_to_question_2: Literal["Male", "Female"]  
    response_to_question_3: Literal[  
        "White",   
        "Black or African American",   
        "American Indian or Alaska Native",   
        "Asian Indian",   
        "Chinese",   
        "Filipino",   
        "Japanese",   
        "Korean",   
        "Vietnamese",   
        "Other Asian",   
        "Native Hawaiian",   
        "Guamanian or Chamorro",   
        "Samoan",   
        "Other Pacific Islander",   
        "Some other race",   
        "REFUSED",   
        "OTHER"  
    ]  
    response_to_question_4: Literal[  
        "Under $10,000",   
        "$10,000 to under $20,000",   
        "$20,000 to under $30,000",   
        "$30,000 to under $40,000",   
        "$40,000 to under $50,000",   
        "$50,000 to under $75,000",   
        "$75,000 to under $100,000",   
        "$100,000 to under $150,000",   
        "$150,000 or more",   
        "DON'T KNOW",   
        "REFUSED",   
        "OTHER"  
    ]  
  
    # Responses for questions 5-11  
    response_to_question_5: Literal[  
        "No formal education",   
        "1st, 2nd, 3rd, or 4th grade",   
        "5th or 6th grade",   
        "7th or 8th grade",   
        "9th grade",   
        "10th grade",   
        "11th grade",   
        "12th grade - NO DIPLOMA",   
        "High school graduate - high school diploma or the equivalent",   
        "Some college, no degree",   
        "Associate degree",   
        "Bachelor's degree",   
        "Master's degree",   
        "Professional or Doctorate degree",   
        "REFUSED",   
        "OTHER"  
    ]  
    response_to_question_6: Literal[  
        "One person, I live by myself",   
        "Two persons",   
        "Three persons",   
        "Four persons",   
        "Five persons",   
        "Six or more persons",   
        "REFUSED",   
        "OTHER"  
    ]  
    response_to_question_7: Literal["DON'T KNOW", "REFUSED", "OTHER"] | int  
    response_to_question_8: Literal["DON'T KNOW", "REFUSED", "OTHER"] | int  
    response_to_question_9: Literal["DON'T KNOW", "REFUSED", "OTHER"] | int  
    response_to_question_10: Literal["DON'T KNOW", "REFUSED", "OTHER"] | int  
    response_to_question_11: Literal["DON'T KNOW", "REFUSED", "OTHER"] | int  
  
    # Responses for questions 12-13  
    response_to_question_12: Literal[  
        "Basically every day",   
        "A few times a week",   
        "A few times a month",   
        "Once a month",   
        "Not at all",   
        "Not sure",   
        "REFUSED",   
        "OTHER"  
    ]  
    response_to_question_13: Literal[  
        "Basically every day",   
        "A few times a week",   
        "A few times a month",   
        "Once a month",   
        "Not at all",   
        "Not sure",   
        "REFUSED",   
        "OTHER"  
    ]  
  
    # Responses for questions 14-18  
    response_to_question_14: Literal[  
        "Not at all or less than 1 day",   
        "1-2 days",   
        "3-4 days",   
        "5-7 days",   
        "DON'T KNOW",   
        "REFUSED",   
        "OTHER"  
    ]  
    response_to_question_15: Literal[  
        "Not at all or less than 1 day",   
        "1-2 days",   
        "3-4 days",   
        "5-7 days",   
        "DON'T KNOW",   
        "REFUSED",   
        "OTHER"  
    ]  
    response_to_question_16: Literal[  
        "Not at all or less than 1 day",   
        "1-2 days",   
        "3-4 days",   
        "5-7 days",   
        "DON'T KNOW",   
        "REFUSED",   
        "OTHER"  
    ]  
    response_to_question_17: Literal[  
        "Not at all or less than 1 day",   
        "1-2 days",   
        "3-4 days",   
        "5-7 days",   
        "DON'T KNOW",   
        "REFUSED",   
        "OTHER"  
    ]  
    response_to_question_18: Literal[  
        "Not at all or less than 1 day",   
        "1-2 days",   
        "3-4 days",   
        "5-7 days",   
        "DON'T KNOW",   
        "REFUSED",   
        "OTHER"  
    ]  
  
    # Responses for questions 19-21  
    response_to_question_19: Literal[  
        "Yes, I worked for someone else for wages, salary, piece rate, commission, tips, or payments 'in kind,' for example, food or lodging received as payment for work performed",   
        "Yes, I worked as self-employed in my own business, professional practice, or farm",   
        "No, I did not work for pay last week",   
        "DON'T KNOW",   
        "REFUSED",   
        "OTHER"  
    ]  
    response_to_question_20: Literal[  
        "Excellent",   
        "Very good",   
        "Good",   
        "Fair",   
        "Poor",   
        "DON'T KNOW",   
        "REFUSED",   
        "OTHER"  
    ]  
    response_to_question_21: Literal[  
        "Yes",   
        "No",   
        "Not sure",   
        "REFUSED",   
        "OTHER"  
    ]  
  
    # Responses for questions 22-31  
    response_to_question_22: Literal["Yes", "No", "Not sure", "REFUSED", "OTHER"]  
    response_to_question_23: Literal["Yes", "No", "Not sure", "REFUSED", "OTHER"]  
    response_to_question_24: Literal["Yes", "No", "Not sure", "REFUSED", "OTHER"]  
    response_to_question_25: Literal["Yes", "No", "Not sure", "REFUSED", "OTHER"]  
    response_to_question_26: Literal["Yes", "No", "Not sure", "REFUSED", "OTHER"]  
    response_to_question_27: Literal["Yes", "No", "Not sure", "REFUSED", "OTHER"]  
    response_to_question_28: Literal["Yes", "No", "Not sure", "REFUSED", "OTHER"]  
    response_to_question_29: Literal["Yes", "No", "Not sure", "REFUSED", "OTHER"]  
    response_to_question_30: Literal["Yes", "No", "Not sure", "REFUSED", "OTHER"]  
    response_to_question_31: Literal["Yes", "No", "Not sure", "REFUSED", "OTHER"]  
  
    # Responses for questions 32-33  
    response_to_question_32: Literal["Yes", "No", "DON'T KNOW", "REFUSED", "OTHER"]  
    response_to_question_33: Literal["REFUSED", "OTHER"] | float 
    
    







def generate_response(conversation, question_count, attempts_per_transcript):
    question_to_reponses = {i:[] for i in range(question_count)} 
    for _ in range(attempts_per_transcript):

        response = client.beta.chat.completions.parse(
                model=os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME'), # model = "deployment_name".
                messages=conversation,
                response_format=SurveyResponses
            )
        responses_in_one_line = response.choices[0].message.content    

        reponse_dict   = json.loads(responses_in_one_line)
        user_responses = []
        for question, answer in reponse_dict.items():
            user_responses.append(answer)
            

        for i in range(question_count):
            answer = user_responses[i]
            question_to_reponses[i].append(answer)

    #print("Here are all of the answers:")
    #print(question_to_reponses)
    finalized_responses = []
    for i in range(question_count):
        counter       = Counter(question_to_reponses[i])
        most_frequent = counter.most_common(1)[0][0]
        finalized_responses.append(most_frequent)

    #print("Final response selections: ")
    #print(finalized_responses)
    return finalized_responses



def infer_answers_to_surveys(role_description, transcripts, question_count, attempts_per_transcript):
    conversation=[{"role": "system", "content": role_description}]
    userid_to_answers = {}
    
    for user_id, transcript in transcripts.items():
        survey = transcript.replace('user:', 'respondent:')
        survey = survey.replace('assistant:', 'surveyor:')
        task_prompt = f"""Help me to understand the following conversation transcript : 
                        {survey}"""
        conversation.append({"role": "user", "content": task_prompt})
        
        person_responses = generate_response(conversation, question_count, attempts_per_transcript)
        userid_to_answers[user_id] = person_responses
        conversation.pop()
    
    return userid_to_answers




def save_answers_to_df(userid_to_answers, codebook, file_name):
    answers_as_list = []
    for user_id in sorted(list(userid_to_answers.keys())):
        answers_as_list.append(userid_to_answers[user_id])
        
        
    question_code_to_text_responses = {}
    i = 0
    for code, val in codebook.items():
        question_code_to_text_responses[code] = []
        for user_answers in answers_as_list:
            response_text = user_answers[i]
            question_code_to_text_responses[code].append(response_text)
        i += 1
    
    df = pd.DataFrame(question_code_to_text_responses)
    
    

    
    df.to_csv(file_name, index=False)
  

    
def analyze_and_save_answers(participant_id, codebook_file = None, transcripts_file = None):
    
    #define necessary directories and files
    if transcripts_file is None and codebook_file is None:
        transcripts_dir   = os.path.join(os.getcwd(), 'transcripts')
        data_dir          = os.path.join(transcripts_dir, f"participant{participant_id}")
        codebook_file     = os.path.join(transcripts_dir, 'codebook.json')
        transcripts_file  = os.path.join(data_dir, 'blandai_transcripts.json')
    
    
    
 
    #get survey details
    QA_details, codebook = get_QA_and_codebook(codebook_file)
    question_count = len(codebook)
    #describe task to gpt
    role_description = f''' You are a diligent assistant tasked with analyzing survey conversation transcripts to deduce the respondent's answers to each of 
                            the {question_count} questions. Ensure that every question has a corresponding answer. Keep in mind the following guidelines:
                                
                                1. Deducing Answers: Responses to specific questions may sometimes be inferred from the broader conversation, even if the question was not explicitly asked. Use context to determine the best possible answer.
                                2. Handling Transcription Errors: Conversations may contain transcription errors. Do your best to interpret the respondent's intended meaning accurately.
                                3. Refusals or Skipped Questions: If the respondent explicitly refuses to answer or skips a question, label the answer as REFUSED. 
                                   Keep in mind that if the respondent explicitly refuses to answer one question, this may sometimes imply a refusal to answer other related questions as well.
                                4. Ambiguity or Non-Matching Responses: If the respondent's answer does not align with any of the predefined response options or is ambiguous, label the answer as OTHER.
                                5. Multiple Responses: If the respondent tells several matching response options within an answer to a question, consider the last response option they give as the final answer.

                            Your goal is to carefully analyze the transcript and assign the most appropriate answer to each question based on the above criteria.
                            
                            Below is the list of questions, each followed on the next line by its corresponding response options separated by semicolons:
                            {QA_details}
                            '''
    
   
    #load transcript for participant and infer answers using gpt
    attempts_per_transcript = 1
    with open(transcripts_file, 'r') as file:
        transcripts = json.load(file)
    userid_to_answers = infer_answers_to_surveys(role_description, transcripts, question_count, attempts_per_transcript)
    
    
    # Save responses deduced by gpt
    gpt_res_dir = os.path.join(os.getcwd(),  'gpt-deductions')
    if not os.path.exists(gpt_res_dir):
        os.makedirs(gpt_res_dir)
    fname  = os.path.join(gpt_res_dir,  f"participant{participant_id}_deduced_{datetime.today().strftime('%Y-%m-%d')}.csv")
    save_answers_to_df(userid_to_answers, codebook, fname)
    
    return fname

if __name__ == '__main__':
    participant_ids = [i for i in range(1, 9)]
    for participant_id in participant_ids:
        print(f"Analyzing participant {participant_id}")
        analyze_and_save_answers(participant_id)
    