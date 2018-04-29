# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 21:25:17 2018

@author: Lacey
"""

#This is the code for finding the sentiment of all the reviews based on the aspects that have been defined
#Food, Service, Ambience and Price
import pandas as pd
import matplotlib.pyplot as plt;
import numpy as np
width = 0.2

#blue = ambience
#red = service
#orange = food
#green = price

if __name__ == "__main__":
    df = pd.read_csv(open("catandsen.csv"), names = ["ambience","food","price","service"])

    x = 1947
    y = 181
    
    objects = ("Positive", "Negative")
    position = np.arange(len(objects))
    performance = (x,y)
    sample = plt.bar(position,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Reviews')
    plt.title("Sentiment Analysis")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    
    a = 18754
    b = 986
    
    objects = ("Positive", "Negative")
    position = np.arange(len(objects))
    performance = (a,b)
    sample = plt.bar(position+(3*width),performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Reviews')
    plt.title("Sentiment Analysis")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    
    d = 98
    e = 3    
    objects = ("Positive", "Negative")
    position = np.arange(len(objects))
    performance = (d,e)
    sample = plt.bar(position+(2*width),performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Reviews')
    plt.title("Sentiment Analysis")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    
    f = 10190
    g = 1332
    
    objects = ("Positive", "Negative")
    position = np.arange(len(objects))
    performance = (f,g)
    sample = plt.bar(position+width,performance,width,align="center",alpha = 0.5)
    plt.xticks(position,objects)
    plt.ylabel('Reviews')
    plt.title("Sentiment Analysis")
    for rect in sample:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    plt.legend("AFPS")
    plt.show()
    plt.savefig("SentimentGraph.png")