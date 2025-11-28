import pandas as pd
import numpy as np

print('WE BEGIN WITH DETECTING OUTLIERS')
df1=pd.read_csv('C:\\Krisha Patel\\ML PROJECTS\\PROJECTS\\retail_store_sales_cleaned.csv')

#OUTLIER RANGE FOR NUMERIC DATA

#PRICE PER UNIT
Q1=df1['Price Per Unit'].quantile(0.25)
Q3=df1['Price Per Unit'].quantile(0.75)
IQR1=Q3-Q1
a=Q1-1.5*IQR1
b=Q3+1.5*IQR1
print('REQUIRED IQR:',IQR1)
print("REQUIRED RANGE FOR 'PRICE PER UNIT' COLUMN:", a,',',b)
outliers_price_per_unit=df1[(df1['Price Per Unit']<(Q1-1.5*IQR1)) | (df1['Price Per Unit']>(Q3+1.5*IQR1))]
print('OUTLIERS IN PRICE PER UNIT COLUMN: \n', outliers_price_per_unit.value_counts().sum())
#Replacing outliers with median value
median1 = df1['Price Per Unit'].median()
df1['Price Per Unit'] = df1['Price Per Unit'].apply(
    lambda x: median1 if x < a or x > b else x
)


#QUANTITY
Q1=df1['Quantity'].quantile(0.25)   
Q3=df1['Quantity'].quantile(0.75)
IQR2=Q3-Q1
c=Q1-1.5*IQR2
d=Q3+1.5*IQR2
print('REQUIRED IQR:',IQR2)
print("REQUIRED RANGE FOR 'QUANTITY' COLUMN:", c,',',d)
outliers_quantity=df1[(df1['Quantity']<(Q1-1.5*IQR2)) | (df1['Quantity']>(Q3+1.5*IQR2))]
print('OUTLIERS IN QUANTITY COLUMN: \n', outliers_quantity.value_counts().sum())
#Replacing outliers with median value
median2=df1['Quantity'].median()
df1['Quantity'] = df1['Quantity'].apply(
    lambda x:median2 if x<c or x>d else x
)


#TOTAL SPENT
Q1=df1['Total Spent'].quantile(0.25)
Q3=df1['Total Spent'].quantile(0.75)
IQR3=Q3-Q1
e=Q1-1.5*IQR3
f=Q3+1.5*IQR3
print('REQUIRED IQR:',IQR3)
print("REQUIRED RANGE FOR 'TOTAL SPENT' COLUMN:", e,',',f)
outliers_total_spent=df1[(df1['Total Spent']<(Q1-1.5*IQR3)) | (df1['Total Spent']>(Q3+1.5*IQR3))]
print('OUTLIERS IN TOTAL SPENT COLUMN: \n', outliers_total_spent.value_counts().sum())
#Replacing outliers with median value
median3=df1['Total Spent'].median()
df1['Total Spent'] = df1['Total Spent'].apply(
    lambda x:median3 if x<e or x>f else x
)
print('OUTLIER DETECTION AND HANDLING IN NUMERIC COLUMNS COMPLETED SUCCESSFULLY!')

df1.to_csv('C:\\Krisha Patel\\ML PROJECTS\\PROJECTS\\retail_store_sales_cleaned.csv', index=False)

df1.info() 

