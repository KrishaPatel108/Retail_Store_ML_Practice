import pandas as pd
import matplotlib.pyplot as plt

#LOAD DATASET
df= pd.read_csv('C:\\Krisha Patel\\ML PROJECTS\\PROJECTS\\retail_store_sales.csv')
print(df.head())
df.info()

#PROBLEMS FOUND:
#1. Null values in Discount applied,item,price per unit,quantity,total spent
#2. Transaction Date is given as Object(datatype)
df.describe()
print('Number of null values in given columns:- ', df.isnull().sum())
#DATA CLEANING
print('Percentage of null values in given columns:- ',df.isnull().sum()/len(df)*100)
df.shape
#Finding Duplicates
print('No. of duplicate rows: ', df.duplicated().sum())
print('NO DUPLICATE ROWS FOUND')
#Handling Null Values
print('PRICE PER UNIT,QUANTITY AND TOTAL SPENT NULL VALUES<5% SO WE DELETE THE ROWS')
df.dropna(subset=['Price Per Unit', 'Quantity', 'Total Spent'], inplace=True)
print('Rows removed successfully!')
#For Discount Applied and Item columns, we will fill null values with mode
df['Discount Applied'] = df['Discount Applied'].fillna(df['Discount Applied'].mode()[0])
df['Item'] = df['Item'].fillna(df['Item'].mode()[0])
print('Null values in Discount Applied and Item columns filled with mode successfully!')
#Converting Transaction Date to datetime datatype
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
print('Transaction Date column converted to datetime datatype successfully! ')

print('Data cleaning completed successfully!')
#Final Check for Null Values
print('Number of null values in given columns after cleaning:- ', df.isnull().sum())

df.to_csv('C:\\Krisha Patel\\ML PROJECTS\\PROJECTS\\retail_store_sales_cleaned.csv', index=False)






