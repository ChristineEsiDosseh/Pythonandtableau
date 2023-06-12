# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:30:29 2023

@author: judit
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Method one to read json data
json_file = open('loan_data_json.json')

data = json.load(json_file)

#Different format to read json data

#with open('loan__data_json.json') as json_file:
#    data = json.load(json_file)
 #   print(data)
    
#Transform to dataframe

loandata = pd.DataFrame(data)

#Finding unique values for the 'purpose' column

loandata['purpose'].unique()

#Brief summary of the data (describing the data)

loandata.describe()

#Describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#Using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#Working with arrays
#ID array
arr = np.array([1, 2, 3, 4])

#0D array
arr = np.array(43)

#2D array
arr = np.array([[1 , 2, 3], [4, 5, 6]])

#Working with IF statements
a = 40
b = 500

if b > a:
    print('b is greater than a')
    
#Let's add more conditions
a = 40
b = 500
c = 1000

if b > a and b < c: 
    print('b is greater than a but less than c')
    
#What is a condition is not met?
a = 40
b = 500
c = 20

if b > a and b < c:
    print('b is greater than a but less than c')
else:
    print('No conditions met')
    
#Another condition, different metrics

a = 40
b = 500
c = 30

if b > a and b < c:
    print('b is greater than a but less than c')
elif b > a and b > c:
    print('b is greater than a and c')
else: 
    print ('No conditions met')

#Using or
a = 40
b = 500
c = 30

if b > a or b < c:
    print('b is greater than a or less than c')
else: 
    print ('No conditions met')

#Modifications
a = 40
b = 0
c = 30

if b > a and b < c:
    print('b is greater than a but less than c')
elif b > a and b > c:
    print('b is greater than a and c')
else: 
    print ('No conditions met')

#Fico Score
fico = 350

#fico >= 300 and < 400: 'Very Poor'
#fico >= 400 and ficoscore < 600: 'Poor'
#fico >= 601 and ficoscore < 660: 'Fair'
#fico >= 660 and ficoscore < 780: 'Good'
#fico >=780: 'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >=601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    fico = 'Good'
elif fico >= 700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)    

#Changing Fico score definition
fico = 250
if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >=601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    fico = 'Good'
elif fico >= 700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)
    
#For loops

fruits = ['apple', 'pear', 'banana', 'cherry'] 

for x in fruits:
    print(x)
    y = x+' fruit'
    print(y)
    
for x in range(0,3):
    y = fruits[x]
    print(y)
    
for x in range(0,4):
     y = fruits[x]
     print(y)   
    
for x in range(0,4):
     y = fruits[x]+' for sale'
     print(y)   
        
#Applying for loops to loan data
#using first 10
length = len(loandata)
ficocat = []
for x in range(0, length):
    category = loandata['fico'][x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >=400 and category <600:
        cat = 'Poor'
    elif category >=600 and category <660:
            cat = 'Fair'
    elif category >=660 and category <700:
        cat = 'Good'    
    elif category >=700: 
        cat = 'Excellent'  
    else:
        cat = 'Unknown'
    ficocat.append(cat)    
ficocat = pd.Series(ficocat) 
loandata['fico.category'] = ficocat

#while loops

i = 1
while i< 10:
    print(i)
    i = i + 1
 
#Using the try command   
 
length = len(loandata)
ficocat = []
for x in range(0, length):
    category = loandata['fico'][x]
    
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >=400 and category <600:
            cat = 'Poor'
        elif category >=600 and category <660:
                cat = 'Fair'
        elif category >=660 and category <700:
            cat = 'Good'    
        elif category >=700: 
            cat = 'Excellent'  
        else:
            cat = 'Unknown'
    except:
           cat = 'Unknown'
           
    ficocat.append(cat)  
    
ficocat = pd.Series(ficocat) 
loandata['fico.category'] = ficocat    
 

#df.loc as conditional statements
#df.loc[df[column name] condition, newcolumnname] = 'value if the condition is met
#for the interest rates, a new column is wanted. rate>0.12 then high, else low
 
loandata.loc[loandata['int.rate'] >0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'    

#number of loans/rows by fico.category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.5)
plt.show()
 
catplot1 = loandata.groupby(['purpose']).size() 
catplot1.plot.bar(color = 'orange', width = 0.3)
plt.show()   
 
#scatter plots

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = '#4caf50')
plt.show()

#Writing to csv
loandata.to_csv('loan_clean.csv', index = True)
    
 