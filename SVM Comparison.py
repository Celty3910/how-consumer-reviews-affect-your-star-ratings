# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 21:19:35 2018

@author: Lacey
"""


# 
import json
import csv
import nltk, string
import numpy as np
from sklearn.preprocessing import normalize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import pandas
from sklearn.model_selection import cross_validate
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_recall_fscore_support
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
import matplotlib.pyplot as plt
stop_words = stopwords.words('english')
wordnet_lemmatizer = WordNetLemmatizer()
import json

# we manully extract out the key words appeared in the food service categories
food_dict = ['Fast Food', 'Delis', 'Sandwiches', 'Soup', 'Steakhouses',
             'Breakfasst & Brunch', 'Seafood', 'Sushi Bars', 'Donuts',
             'Ice Cream & Frozen Yogurt', 'Cupcakes', 'Chicken Wings', 'Asian Fusion',
             'Mexican', 'Chinese', 'American', 'Japanese', 'Canadian', 'French',
             'Waffles','Juice','Bars','Smoothies','Hot Dogs','Fish','Chips',
             'Bagels','Salad','Soup','Ramen','Vegetarian','Barbeque','Gluten-Free',
             'Buffets','Cafes','Caterers']

def svc(reviews, business_id):
    tfidf_vect = TfidfVectorizer(stop_words = "english")
    dtm = tfidf_vect.fit_transform(reviews)
    metrics = ['precision_macro', 'recall_macro', "f1_macro"]
    
    #calculate the svc() value for the assignment
    clf = svm.LinearSVC()
    cv = cross_validate(clf, dtm, business_id, scoring=metrics, cv=5)
    print(" ")
    print("Output for Reviews by Business Id")
    print("Test data set average precision:")
    print(cv['test_precision_macro'])
    print("\nTest data set average recall:")
    print(cv['test_recall_macro'])
    print("\nTest data set average fscore:")
    print(cv['test_f1_macro'])
    
    avg_pre = np.average(cv['test_precision_macro'])
    avg_rec = np.average(cv['test_recall_macro'])
    avg_f1 = np.average(cv['test_f1_macro'])
    print (avg_pre, avg_rec, avg_f1)

#
if __name__ == "__main__":
    data = {}
    business_id =[]
    categories = []
    star = []
    i = 0
    with open("business.json") as json_file:
        try:
            for line in json_file:
                line_contents = json.loads(line)
                business_id.append(line_contents['business_id'])
                categories.append(line_contents['categories'])
                star.append(line_contents['stars'])
                i += 1
        except UnicodeDecodeError:
            print("failed to parse data")
            pass
    
    data = dict(zip(business_id, categories))  
    #print (star)
    #file = csv.writer(open("sample.csv","w" ))
    #file.writerow(map(lambda x: [x], star))
    data1 = {}
    keys_id = []
    values_id = []
    
    for key, values in data.items():
        for x in food_dict:
            if x in values:
                keys_id.append(key)
                values_id.append(values)
    data1 = dict(zip(keys_id, values_id))
    
    #print data1
    print (len(data1))
    #print (type(categories))
    #print food_dict
    #print(len(business_id))
    #print(data)
    print('\n')
    
    b_id =[]
    b_text = [] 
    j = 0
    with open("review.json") as json_file:
        try:
            for l in json_file:
                l_contents = json.loads(l)
                b_id.append(l_contents['business_id'])
                b_text.append(l_contents['text'])
                j += 1
                #print(len(set(b_id)))  # output 156,638
                #print(b_text)     # output 4,736,897
                
        except UnicodeDecodeError:
            print("failed to parse data")
            pass
    #print(b_id)
    #print(len(set(b_id)))
    
    review_data = dict(zip(b_id, b_text))
    svc(b_text, b_id)
    #print (len(review_data))