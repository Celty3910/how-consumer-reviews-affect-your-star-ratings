# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 14:01:29 2018

@author: Lacey
"""

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
# the following part of code may takes at least half an hour to 3 hours depends on your machime.
# we don't run it over here
# but the out put is included in the folder

import subprocess
import json
import csv
import re
import codecs


import time
start_time = time.time()

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from sklearn.preprocessing import normalize
from nltk.corpus import stopwords





############################################################
# NOTES:
# split big json into smaller chunks
# split -b 800mb review.json
#
# merge files into one
# cat *.csv >merged.csv



###################################################################################
# Step I.  Filtering out the FOOD service related text reviews
##################################################################################



# we manully extract out the key words appeared in the food service categories
food_dict = ['Fast Food', 'Delis', 'Sandwiches', 'Soup', 'Steakhouses',
             'Breakfasst & Brunch', 'Seafood', 'Sushi Bars', 'Donuts',
             'Ice Cream & Frozen Yogurt', 'Cupcakes', 'Chicken Wings', 'Asian Fusion',
             'Mexican', 'Chinese', 'American', 'Japanese', 'Canadian', 'French',
             'Waffles','Juice','Bars','Smoothies','Hot Dogs','Fish','Chips',
             'Bagels','Salad','Soup','Ramen','Vegetarian','Barbeque','Gluten-Free',
             'Buffets','Cafes','Caterers']

data = {}
business_id =[]
categories = []
i = 0
print('\n')
print('Start reading business.json')
print('......')
print('\n')
with codecs.open('business.json','rU','utf-8') as json_file:
    try:
        for line in json_file:
            line_contents = json.loads(line)
            business_id.append(line_contents['business_id'])
            categories.append(line_contents['categories'])
            i += 1
            #print (line_contents['business_id'], line_contents['categories'])
    except UnicodeDecodeError:
        print("failed to parse data")
        pass

print('finish reading business.json')
print('\n')


# make a dictionary that business_id as keys and
# the corresponding categories as values
data = dict(zip(business_id, categories))

food_data = {}
food_id = []
#food_categories = []

# filter out all FOOD related services
for business_id, categories in data.items():
    for elem in food_dict:
        if elem in categories:
            food_id.append(business_id)
            #food_categories.append(categories)
#food_data = dict(zip(food_id, food_categories))


print (len(food_id))


review_busi_id =[]
review_text = []
stars = []
#j = 0
print('Start reading reviews.json')
print('......')
# extract only the text review and its corresponding text review part
with codecs.open('review.json','rU','utf-8') as json_file:
    try:
        for l in json_file:
            l_contents = json.loads(l)
            review_busi_id.append(l_contents['business_id'])
            review_text.append(l_contents['text'])
            stars.append(l_contents['stars'])
            #j += 1
            #print (j, l_contents['text'])
            #print ("\n")
        #print ('size: ', len(review_text))
    except UnicodeDecodeError:
        print("failed to parse data")
        pass

print('\n')
print('finish reading reviews.json')
print('\n')

print('Start saving food_reviews.csv')
print('......')
# dictionary with b_id as keys and b_text as values
review_data = dict(zip(review_busi_id, review_text))
review_stars = dict(zip(review_busi_id, stars))
f_1 = csv.writer(open('food_reviews_1.csv','w'))
f_2 = csv.writer(open('food_reviews_2.csv','w'))
#output1 = []
idx = 0
# only FOOD-service related reviews
for id in food_id:
    for review_busi_id, review_text in review_data.items():
        if  review_busi_id == id:
                print (idx, review_busi_id)
                f_1.writerow([review_busi_id,review_text])
                #output1.append(review_text)
                print (idx, review_text)
                idx += 1
                print ('\n')
            
    for review_bid, stars in review_stars.items():
        if  review_id == id:
                print (idx, review_busi_id)
                f_2.writerow([review_busi_id,stars])
                #output1.append(review_text)
                print (idx, stars)
                #idx += 1
                print ('\n')

#f.close()
#print output1
#print('\n')
#print('finish saving food_reviews.csv')
#print('\n')


