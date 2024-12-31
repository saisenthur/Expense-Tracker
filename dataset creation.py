import pandas as pd
import random
import os
import warnings
from faker import Faker
from sqlalchemy import create_engine
from datetime import datetime

warnings.filterwarnings('ignore')

fake = Faker()

categories = ['Food', 'Transportation', 'Bills', 'Entertainment', 'Shopping', 'Healthcare','Investments','Loans','Fuel']
categories_dic = {
    'Food': ['Swiggy','Zomato','Dine in'],
    'Transportation': ['Train','Bus','Flight','Metro Train'],
    'Bills': ['Netflix','Water','Electricity','Tax','Creditcard','Insurance'],
    'Entertainment': ['Movie','Gaming','Sports'],
    'Shopping': ['Clothes','Groceries','Snacks','Accessories','Online shopping'],
    'Healthcare':['Medicine','Clinic fees'],
    'Investments':['Stocks','Mutual funds','Gold','FD'],
    'Loans': ['Student','Personal','Housing'],
    'Fuel': ['Fuel']
              }
payment_modes = ['Cash','UPI','Credit_Card']
columns = ["Date", "Category", "Description", "Payment_Mode", "Amount_Paid", "Cashback"]
merge_df = pd.DataFrame(columns=columns)

# Directory to save CSV files
output_dir = "monthly_expenses"
os.makedirs(output_dir, exist_ok=True)

# Function to generate a dataset for a given month
def generate_monthly_expenses(year, month):
    days_in_month = 30 if month in [4, 6, 9, 11] else 31
    if month == 2:
        days_in_month = 28  # Assuming no leap year
    num_transactions = random.randint(100, 150)  # Random number of transactions in a month

    data = {
        "Date": [
            f"{year}-{month:02d}-{random.randint(1, days_in_month):02d}"  #to be checked
            for _ in range(num_transactions)
        ],
        "Category": [random.choice(categories) for _ in range(num_transactions)],
        # "Description": [fake.word() for _ in range(num_transactions)],
        "Payment_Mode": [random.choice(payment_modes) for _ in range(num_transactions)],    
        "Amount_Paid": [round(random.uniform(10, 500), 2) for _ in range(num_transactions)],
        "Cashback": [ 
            round(random.uniform(0, 20), 2) if random.choice([True, False]) else 0 
            for _ in range(num_transactions)
        ],
    }
    data['Description'] = [ random.choice(categories_dic[i]) for i in data['Category'] ]
        
    return pd.DataFrame(data)

# Generate datasets for each month and save them
year = 2024
for month in range(1, 13):  # Loop through 12 months
    df = generate_monthly_expenses(year, month) #calling the function to create data set using Faker
    merge_df=pd.concat([merge_df,df], ignore_index=True) #merging to one single file
    file_path = os.path.join(output_dir, f"expenses_{year}_{month:02d}.csv")
    df.to_csv(file_path, index=False) # converting dataframe to csv file
    print(f"Saved: {file_path}")

print(f"All monthly expense tables have been saved in the '{output_dir}' directory.")

merge_df['Date'] = pd.to_datetime(merge_df['Date'])
merge_df['Month']=merge_df['Date'].dt.month

merge_df.to_csv("expenses_2024_master.csv", index=False)