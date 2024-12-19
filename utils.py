#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 13:13:11 2024

@author: kaiyrbekovk2
"""
import pandas as pd
import json


codebook_file = './associatedpress-covid-impact-survey-public-data/COVID survey data codebook.csv'




class QA():
    def __init__(self, question):
        self.question = question
        self.answers = {}
    def set_answers(self, answer, description):
        self.answers[answer] = description
    def get_answer(self, answer_id):
        return self.answers[answer_id]
    def get_question(self):
        return self.question
    def __str__(self):
        str_rep = 'Question: ' + self.question + '\n' + 'Answer options:'
        for key in sorted(self.answers):
            #option = '%g %s' %(key, self.answers[key])
            str_rep  += '\n' + str(self.answers[key])
        return str_rep
    
    def to_json_dictionary(self):
        json_dict = {}
        json_dict["question"] = self.question
        json_dict["answer_to_answer_id"] = {}
        for asnwer_id, answer_text in self.answers.items():
            #print(answer_text)
            #answer_text.index(')')
            text = answer_text[answer_text.index(')')+1:].strip()
            json_dict["answer_to_answer_id"][text] = asnwer_id
        return json_dict

    
    
def get_codebook():
    codebook_df = pd.read_csv(codebook_file)
    codebook = {}
    code = None
    num_questions = 0
    for index, row in codebook_df.iterrows():
        #print(pd.isna(row['Variable']), row['Variable Label'], row['Value'], vals['Value Label'])
        #print(row['Value Label'])
        ans_id          = row['Value']
        ans_description = row['Value Label']
        ans_id = int(ans_id) if isinstance(ans_id, (int, float)) and not pd.isna(ans_id) else ans_id
        if pd.isna(row['Variable']):
            codebook[code].set_answers(ans_id, ans_description)
        else:
            num_questions += 1
            #if num_questions >= 8:
            #    print(codebook[code].question)
            code = row['Variable']
            codebook[code] = QA(row['Variable Label'])
            #ans_id          = row['Value']
            #print(ans_id)
            #if isinstance(ans_id, (int, float)): print(ans_id)
            
            #print(ans_id)
            ans_description = row['Value Label']
            codebook[code].set_answers(ans_id, ans_description) #turn to int?
           
    return codebook


def get_questions_list(codebook, codes):
    N = len(codes)
    return '\n'.join([ '%d. %s' %(i+1, codebook[codes[i]].get_question()) for i in range(N)])

def get_codebook_subset(codebook, codes):
    new_codebook = {}
    for code in codes:
        new_codebook[code] = codebook[code]
    return new_codebook

def codebook_to_json(codebook, codebook_file_name = 'codebook.json'):
    cb_json = {}
    for code, info in codebook.items():
        cb_json[code] = codebook[code].to_json_dictionary()
        
    with open(codebook_file_name, "w") as f:
        f.write(json.dumps(cb_json))


#questions = get_questions_list(codebook, ['SOC1',	'SOC2A', 'SOC2B', 'SOC3A',	'SOC3B',	'SOC4A',	'SOC4B',	'PHYS8',	'PHYS1A',	'PHYS1B'])
#print(questions)

#json.dump(codebook, 'cb.json')

#json.dumps(codebook['SOC1'].toJSON())

if __name__ == '__main__':
    codebook = get_codebook()
    print(codebook['SOC1'].answers)
    print(codebook['SOC1'].to_json_dictionary())