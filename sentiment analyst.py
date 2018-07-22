# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:26:00 2018

@author: cuity328
"""
import json
import bz2file
import os
import re
#traverse all the folder
def traverse(rootdir):
    file_list = []
    for root,dirs,files in os.walk(rootdir):
        for f in files:
            file_list.append(os.path.join(root,f))
        for d in dirs:
            traverse(d)
    return file_list


# clean and get the data in each file and accumulate the number of retweet and favorite in this file
def load_single_file(file_str):
    textset=[]
    retweet=0
    favorite=0
    infile= bz2file.open(file_str,'r') 
    lines = infile.readlines()
    data_list = map(json.loads,lines)
    cleanr=re.compile('(@[A-Za-z0-9]+)|([^0-9A-Za-z\t])|(\w+:\/\/\S+)')
    for data in data_list:
        if 'text' in data:
            try:
                if 'blockchain' in data['text'].lower():
                    cleantext=re.sub(cleanr,' ',data['text']).split()
                    textset.append(cleantext)
                    retweet+=data['retweet_count']
                    favorite+=data['favorite_count']
            except:
                pass
    return textset,retweet,favorite


#generate random sample
import random
leng=len(traverse('E:\\sentiment analyst'))
i=random.sample(range(leng),leng/3)
final_text=[]
retweet_count=0
favorite_count=0
for t in i:
    word,r,f=load_single_file(traverse('E:\\sentiment analyst')[t])
    final_text.append(word)
    retweet_count+=r
    favorite_count+=f


#use textblob package to get sentiment
from textblob import TextBlob
def sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'
        

#count amount of sentiment  
positive_count=0
negative_count=0
neutural_count=0  
for row in final_text:
    if sentiment(row) is 'positive':
        positive_count+=1
    elif sentiment(row) is 'neutral':
        neutural_count+=1 
    else:
        negative_count+=1  
        

print 'retweet_count=:',retweet_count
print 'favorite_count=:',favorite_count
print 'positive_count=:',positive_count
print 'negative_count=：',negative_count
print 'neutural_count=:',neutural_count
    
    
    