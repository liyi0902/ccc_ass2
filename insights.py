# -*- coding: utf-8 -*-
"""
@author: mohnishdevadiga
"""

import pickle
import json
import gender as g
import trying_anger as anger
import re

# Calssifier for Gender prediction
with open('data/Gender.pkl', 'rb') as f:
    gclassifier = pickle.load(f)

# Classifier for anger detection in sentence
with open('data/Anger.pkl', 'rb') as f1:
    aclassifier = pickle.load(f1)
#Counter Vector for anger detection
with open('data/Acv.pkl', 'rb') as f2:
    acv = pickle.load(f2)

"""
    
"""
def get_data(read_line):
    data_list = []
    #print(read_line)
    try:
        if read_line.endswith(',\n'):
            val = len(read_line)
            temp_json = json.loads(read_line[:val - 2])

        elif read_line.endswith('\n'):
            val = len(read_line)
            temp_json = json.loads(read_line[:val - 1])

        if bool(temp_json['doc']['coordinates']['coordinates']):
            data_list.append(temp_json['doc']['user']['name'].split())
            data_list.append(temp_json['doc']['coordinates']['coordinates'][0])
            data_list.append(temp_json['doc']['coordinates']['coordinates'][1])
            data_list.append(temp_json['doc']['text'])
            anger.contains_angry(temp_json['doc']['text'])
        else:
            pass
    except:
        pass

    return (data_list)


"""
Send as a list as some twitter user names have names such as "Mr. Dan Brown"
returns 'male' or 'female'
"""
def get_gen(lst):
    if type(lst) == type(''):
        lst = lst.split()
    for word in lst:
        #cleaning names
        word = re.sub(r'[^\w]', ' ', word) # only words
        word = word.strip()
        if word.isalpha():
            return(gclassifier.classify(g.features(word)))
                            

"""
Send a sentence will predict as 0 or 1:
0: not-angry
1: angry
"""
def is_angry(sent): # 0 means not angry 1 means angry
    X_test = acv.transform([sent]).toarray()
    y_pred = aclassifier.predict(X_test)
    return(y_pred[0])

