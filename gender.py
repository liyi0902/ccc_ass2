# -*- coding: utf-8 -*-
"""
@author: mohnishdevadiga
"""

import nltk
import random
import pickle
import re


def features(name):
    try:
        word = name.lower()
        #cleaning errors if in male or female txt files
        word = re.sub(r'[^\w]', ' ', word) # only words
        word = word.strip()
        if len(name) >= 3:
            return {'1': word[0],
                    '2': word[0:2],
                    '3': word[0:3],
                    '-1': word[-1],
                    '-2': word[-2:],
                    '-3': word[-3:]
                    }
        else:
            return {"pair": word[-2:]}
    except Exception as e:
        print(e)
        pass
               

male = open('data/male.txt', 'r')
maleLst = [(features(i),'male') for i in set(male.read().split(','))]
female = open('data/female.txt', 'r')
femaleLst = [(features(i),'female') for i in set(female.read().split(','))]

names = list(maleLst + femaleLst)
random.shuffle(names)
training_set = names[:int(len(names)*0.7)]
test_set = names[:int(len(names)*0.3)]

classifier = nltk.NaiveBayesClassifier.train(training_set)
accuracy = nltk.classify.accuracy(classifier, test_set)

#saving classifier
with open('data/Gender.pkl', 'wb') as f:
    pickle.dump(classifier, f)
