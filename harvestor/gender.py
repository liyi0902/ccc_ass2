# -*- coding: utf-8 -*-


import nltk
import random
import pickle
import re


def features(name):
    try:
        word = name.lower()
        # cleaning errors if in male or female txt files
        word = re.sub(r'[^\w]', ' ', word)  # only words
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
