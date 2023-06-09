# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 15:10:06 2023

@author: judit
"""

import pandas as pd

#file_name = pd.read_csv('file.csv')<....... format_csv

data = pd.read_csv('transaction2.csv')

data = pd.read_csv('transaction2.csv',sep=';')

#summary of the data 

data.info()

#working with calculations

#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemPurchased = 6

#Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemPurchased * ProfitPerItem
SalesPerTransaction = SellingPricePerItem * NumberOfItemPurchased
CostPerTransaction = CostPerItem * NumberOfItemPurchased

#CostPerTransaction Column Transaction
#CostPerTransaction = CostPerItem * NumberofItemPurchased
#Variable = dataframe ['column_name']

CostPerItem = data['CostPerItem']

NumberOfItemPurchased = data['NumberOfItemsPurchased']

CostPerTransaction = CostPerItem * NumberOfItemPurchased

#Adding new column to dataframe

data['CostPerTransaction'] = CostPerTransaction 
#Other option of doing the above

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit calculation = Sales - Cost

data['ProfitperTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = Sales - Cost/Cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

#Another way of doing markup

data['Markup'] = (data['ProfitperTransaction']) / data['CostPerTransaction']

#Rounding markup

roundmarkup = round(data['Markup'], 2)

data['Markup'] = round (data['Markup'], 2)

#Combining data fields

my_name = 'Christine'+'Dosseh'

my_date = 'Day'+'-'+'Month'+'-'+'Year'

#Checking columns data type

print(data['Day'].dtype)

#Change Columns type

day = data['Day'].astype(str)

year = data['Year'].astype(str)

print(day.dtype)

print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date

#Using iloc to view specific columns and rows

data.iloc[0] #views the row with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 3 rows

data.head(5) #Brings in first 5 rows

data.iloc[:,2] #brings in all rows on the 2nd column
data.iloc[4,2] #brings in 4th row, 2nd column 

#using the split function to split client_keywords field
#new_var = coliumn.str.split('sep' , expand = true)

split_col = data['ClientKeywords'].str.split(',' , expand=True) 

#Creating new columns for the split columns in Client Keywords

data['ClientAge'] = split_col[0] 
data['ClientType'] = split_col[1] 
data['LenthofContract'] = split_col[2] 

#Using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')

data['LenthofContract'] = data['LenthofContract'].str.replace(']' , '')

#Using the lower function to  change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#How to merge files
#bringing in a new dataset


seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#Merging files:mer_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#Dropping a few columns 

#df = df.drop('columnname' , axis = 1)

data = data.drop('ClientKeywords' , axis = 1)

data = data.drop('Day' , axis = 1)
data = data.drop('Year' , axis = 1)
data = data.drop('Month' , axis = 1)

#Or drop them in one line
data = data.drop(['Year' , 'Day' , 'Month'], axis = 1)

#Export into CSV

data.to_csv('ValueInc_Cleaned.csv' , index = False)

#End of project 1








