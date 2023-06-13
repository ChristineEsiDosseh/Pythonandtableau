# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:55:04 2023

@author: judit
"""


import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 

#Reading excell or xlsx files
data = pd.read_excel('articles.xlsx')

#summary of the data
data.describe()

#summary of the columns
data.info()

#counting the number of articles per source
#format of groupby: df.groupby(['column_to_group'])['column to count or sum'].count()

data.groupby(['source_id'])['article_id'].count()

#Number of reactions by publisher

data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping a column
data = data.drop('engagement_comment_plugin_count' ,axis=1)

#Functions in Python

def thisFunction():
    print('This is my First Function')
thisFunction()

#This is a function with variables

def aboutMe(name, surname, location):
    print('This is '+name+' My surname is '+surname+' I am from '+location)
    return name, surname, location
    
C = aboutMe('Christine', 'Nkyaagye', 'United States of America')

#Using for loops in functions

def favfood(food):
    for x in food:
        print('Top food is '+x)

fastfood = ['Waakye', 'Jollof', 'Fufu']

favfood(fastfood)

#Creating a keyword flag

keyword = 'crash'
#Let's create a for loop to isolate each title

#length = len(data)
#keyword_flag = []
#for x in range(0, length):
#    heading = data['title'][x]
#    if keyword in heading:
#        flag = 1
#    else:
#        flag = 0
#    keyword_flag.append(flag)
        
#Creating a function        
        
def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag

keywordflag = keywordflag("support")
    
#Creating a new column in the data dataframe

data['keyword_flag'] = pd.Series(keywordflag)         

#SentimentIntensityAnalyzer 

sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']


#Adding a for loops to extract sentiment per title

title_neg_sentiment =[]
title_pos_sentiment =[]
title_neu_sentiment =[]

length = len(data)

for x in range(0, length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except: 
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment        
data['title_neu_sentiment'] = title_neu_sentiment        
        
#Writing the dat
data.to_excel('BlogMe_clean.xlsx', sheet_name='blogdata', index=False)



