import streamlit as st
import pandas as pd
import mysql
from mysql import connector
import matplotlib.pyplot as plt

st.title("Expense Tracker 	:heavy_dollar_sign: :money_with_wings: :chart: ")

st.write("This Web application shows the EDA done on the expense data")

df=pd.read_csv("C:/Users/saisenthur/OneDrive/Desktop/Guvi/Project/Expense tracker/expenses_2024_master.csv")

#MySQL connector
con = connector.connect(
    host="localhost",
    user="root",
    password="Saisenthur@13"
    #database="Expense_tracker"
    )
#st.write(con)
mycursor=con.cursor()

mycursor.execute('USE Expense_tracker')

#1)Month wise expenses

st.write('### 1) Month wise Expense :calendar:')
mycursor.execute("select month(date) as Month, sum(amount_paid) as Total  from expense_2024 group by month(date)")
data=mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]  # Extract column names from the query result
df1 = pd.DataFrame(data, columns=columns)

st.table(df1)

month_df=df.groupby('Month')[['Amount_Paid']].sum()

st.write('### Month Line graph :calendar:')
plt.figure(figsize=(10, 5)) 
x = month_df.index
y = month_df['Amount_Paid']
plt.plot(x, y, marker='o', label='Line')
# Add labels, title, and legend
plt.xticks(range(0, max(x) + 1, 1))
plt.xlabel('Month')
plt.ylabel('Amount_Spent')
plt.title('Simple Line Plot')
plt.legend()
plt.grid(True)
st.pyplot(plt)

plt.clf()

#2)Category wise expenses

st.write('### 2) Category wise Expense')
mycursor.execute("select Category, sum(amount_paid) as Total from expense_2024 group by category")
data=mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]  # Extract column names from the query result
df2 = pd.DataFrame(data, columns=columns)

st.table(df2)   

# plt.figure(figsize=(10, 5)) 
plt.bar(df2['Category'], df2['Total'], color='red')
# Add labels and title
plt.xlabel('Categories', labelpad=30)
plt.ylabel('Values')
plt.title('Category wise Expense')
plt.tight_layout()
st.pyplot(plt)

plt.clf()



#3)mode of payment wise Expenses
st.write('### 3) Mode of Payment wise Expenses')
mycursor.execute("select Payment_mode , sum(Amount_paid) as Total_Expenses  from expense_2024 group by Payment_mode")
data=mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]  # Extract column names from the query result
df3 = pd.DataFrame(data, columns=columns)

st.table(df3)

st.write('### Payment Mode :credit_card: :dollar:')
plt.pie(df3['Total_Expenses'], labels=df3['Payment_mode'], autopct="%1.1f%%", startangle=90)
plt.title('Pie Chart')
st.pyplot(plt)
plt.clf()

#4) the variation between transportation and fuel expenses compared
st.write('### 4) Variation between transportation & fuel expenses compared :')
st.write('### Transport Expenses')
T_df=df[df['Category']=='Transportation']
Transport_df=T_df.groupby('Month')[['Amount_Paid']].sum()
Transport_df= Transport_df.rename(columns={'Amount_Paid': 'Transport Expenses'})
st.area_chart(Transport_df)

st.write('### Fuel Expenses')
F_df=df[df['Category']=='Fuel']
Fuel_df=F_df.groupby('Month')[['Amount_Paid']].sum()
Fuel_df= Fuel_df.rename(columns={'Amount_Paid': 'Fuel Expenses'})
st.area_chart(Fuel_df)

st.write('### Total Travel Expenses')
travel_df=pd.merge(Transport_df,Fuel_df, left_index=True, right_index=True)
st.write(travel_df)
st.area_chart(travel_df[['Transport Expenses','Fuel Expenses']])

#5)category wise cashback
st.write('### 5) Category wise Cashback')
mycursor.execute("select category as Category, sum(cashback) as Total_cashback  from expense_2024 group by category")
data=mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]  # Extract column names from the query result
df5 = pd.DataFrame(data, columns=columns)

st.table(df5)


#6)
st.write('### 6) Investments')
mycursor.execute("select Description,sum(Amount_Paid) as 'Amount Invested' from expense_2024 where category='Investments' group by description")
data=mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]  # Extract column names from the query result
df6 = pd.DataFrame(data, columns=columns)

st.table(df6)

#7)
st.write('### 7) Transportation Expenses')
mycursor.execute("select Description as 'Mode of Transportation',sum(Amount_Paid) as 'Total Expenses' from expense_2024 where category='Transportation' group by description")
data=mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]  # Extract column names from the query result
df7 = pd.DataFrame(data, columns=columns)

st.table(df7)


#8)
st.write('### 8) Food Expenses')
mycursor.execute("select Description as 'Food Expenses',sum(Amount_Paid) as Total from expense_2024 where category='Food' group by description")
data=mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]  # Extract column names from the query result
df8 = pd.DataFrame(data, columns=columns)

st.table(df8)

#9)
st.write('### 9) Hotel Food Expenses each month')
mycursor.execute("select month as Month,  sum(Amount_paid) as 'Amount_Spent', count(description) as 'Count of hotel food' from expense_2024 where category = 'Food' group by month")
data=mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]  # Extract column names from the query result
df9 = pd.DataFrame(data, columns=columns)

st.table(df9)

#10)
st.write('### 10) Loan Expenses')
mycursor.execute("select Description,  sum(Amount_paid) as 'Loan Amount' from expense_2024 where category = 'Loans' group by description")
data=mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]  # Extract column names from the query result
df10 = pd.DataFrame(data, columns=columns)

st.table(df10)

st.write('### Loan Expenses')
plt.pie(df10['Loan Amount'], labels=df10['Description'], autopct="%1.1f%%", startangle=90)
plt.title('Pie Chart')
st.pyplot(plt)
plt.clf()

#11)
st.write('### 11) Clinic visits and fees')
mycursor.execute("select Month, count(description) as 'Number of clinic visits', sum(Amount_paid) as 'Total fees' from expense_2024 where description = 'Clinic fees' group by month")
data=mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]  # Extract column names from the query result
df11 = pd.DataFrame(data, columns=columns)

st.table(df11)

#12)
st.write('### 12) Entertainment expenses :video_game: :cinema: :performing_arts:')
mycursor.execute("select Month, sum(Amount_paid) as 'Total expenses' from expense_2024 where Category = 'Entertainment' group by month")
data=mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]  # Extract column names from the query result
df12 = pd.DataFrame(data, columns=columns)

st.table(df12)

#13)
st.write('### 13) Number of Movies watched and Expenses :cinema: :movie_camera:')
mycursor.execute("select Month, count(Description) as 'Number of movies watched', sum(Amount_paid) as 'Total expenses' from expense_2024 where Description = 'Movie' group by month")
data=mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]  # Extract column names from the query result
df13 = pd.DataFrame(data, columns=columns)

st.table(df13)

#14)
st.write('### 14) Shopping Expenses')
mycursor.execute("select Description, sum(Amount_paid) as 'Total expenses' from expense_2024 where category = 'Shopping' group by description")
data=mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]  # Extract column names from the query result
df14 = pd.DataFrame(data, columns=columns)

st.table(df14)  

#15)
st.write('### 15) Monthly Shopping Expenses')
mycursor.execute("select Month, sum(Amount_paid) as 'Total expenses' from expense_2024 where category = 'Shopping' group by month;")
data=mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]  # Extract column names from the query result
df15 = pd.DataFrame(data, columns=columns)

st.table(df15)  

#16)
st.write('### 16) Bill Expenses')
mycursor.execute("select Description, sum(Amount_paid) as 'Total expenses' from expense_2024 where category = 'Shopping' group by description;")
data=mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]  # Extract column names from the query result
df16 = pd.DataFrame(data, columns=columns)

st.table(df16) 

#17)
st.write('### 17) Bill Expenses monthly')
mycursor.execute("select Month, sum(Amount_paid) as 'Total expenses' from expense_2024 where category = 'Shopping' group by month;")
data=mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]  # Extract column names from the query result
df17 = pd.DataFrame(data, columns=columns)

st.table(df17) 







