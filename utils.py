#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 13:13:11 2024

@author: kurmanbek
"""
import pandas as pd
import json
import copy


codebook_file = './associatedpress-covid-impact-survey-public-data/COVID survey data codebook.csv'




class QA():
    def __init__(self, question):
        self.question = question
        self.response_id_to_text = {}
        self.response_text_to_id = {}
    def set_answers(self, response_id, response_text):
        self.response_id_to_text[response_id] = response_text
        
        self.response_text_to_id[response_text] = response_id
        
    def get_response_text(self, response_id):
        if response_id not in self.response_id_to_text:
            print("Response might be numeric, so returning original input")
            return response_id
        return self.response_id_to_text[response_id]
    
    def get_response_id(self, response_text):
        return int( self.response_text_to_id[response_text])

    def get_question(self):
        return self.question
    def __str__(self):
        str_rep = 'Question: ' + self.question + '\n' + 'Answer options:'
        for key in sorted(self.response_id_to_text):
            #option = '%g %s' %(key, self.answers[key])
            str_rep  += '\n' + str(self.response_id_to_text[key])
        return str_rep
    
    def to_json_dictionary(self):
        json_dict = {}
        json_dict["question"] = self.question
        json_dict["clean_response_text_to_id"] = {}
        json_dict["response_id_to_text"] = copy.copy(self.response_id_to_text)
        for answer_id, answer_text in self.response_id_to_text.items():
            #print(answer_text)
            #answer_text.index(')')
            text = answer_text.strip()
            if ')' in answer_text:
                text = answer_text[answer_text.index(')')+1:].strip()
            json_dict["clean_response_text_to_id"][text] = answer_id
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
    print(codebook['HHINCOME'].response_id_to_text)
    print(codebook['HHINCOME'].to_json_dictionary())
    print(codebook['SOC1'].get_response_id('(4) None'))