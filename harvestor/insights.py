# -*- coding: utf-8 -*-

import pickle
import json
import gender as g
from textblob import TextBlob
from sklearn.externals import joblib
import os

import re
import shapely.geometry

project_Path ="/home/ubuntu/harvestor"

with open(project_Path+"/Gender_py2.pkl", 'rb') as f:
    gclassifier = pickle.load(f)


# with open(path+'Anger_py2.pkl', 'rb') as f1:
#     aclassifier = pickle.load(f1)
# with open(path+'Acv_py2.pkl', 'rb') as f2:
#     acv = pickle.load(f2)


with open(project_Path + '/Anger.pkl', 'rb') as f1:
    aclassifier = joblib.load(f1)
with open(project_Path +'/Acv.pkl', 'rb') as f2:
    acv = joblib.load(f2)
with open(project_Path +'/Ecv_py2.pkl','rb') as f4:
    ecv = joblib.load(f4)

with open(project_Path +"/lga-vic.json", 'r') as l:
    location = json.load(l)



def get_gen(lst):
    if type(lst) == type(" "):
        lst = lst.split()
    for word in lst:
        # cleaning names
        word = re.sub(r'[^\w]', ' ', word)  # only words
        word = word.strip()
        if word.isalpha():
            return (gclassifier.classify(g.features(word)))


# def is_angry(sent):  # 0 means not angry 1 means angry
#     X_test = acv.transform([sent.lower()]).toarray()
#     y_pred = aclassifier.predict(X_test)
#     return (y_pred[0])


def is_angry(sentence):  # 1 means negative, -1 means positive, and 0 means mild
    svm_value = svm_analysis(sentence)
    textblob_value = textblob_analysis(sentence)
    sum = svm_value + textblob_value * (-1)
    if (sum <= 2) & (sum >= 0.8):
        return '1'
    elif (sum >= -2) & (sum <= -0.8):
        return '-1'
    else:
        return '0'


def svm_analysis(sentence):
    X_test = acv.transform([sentence.lower()]).toarray()
    y_pred = aclassifier.predict(X_test)
    return float(y_pred[0])


def textblob_analysis(sentence):
    textblob = TextBlob(sentence.decode('utf-8'))
    value = textblob.sentiment
    return value[0]


def get_location(lst):
    try:
        #lst.reverse()
        point = shapely.geometry.Point(lst)
        for i in location:
            polygon = shapely.geometry.Polygon(location[i]['geometries'][0]['coordinates'][0][0])
            if point.within(polygon):
                return i
    except:
        return None
