drop database expense_tracker;

use expense_tracker;

select*from expense_2024;

# 1)
select month(date) as Month, sum(amount_paid) as Total  from expense_2024 group by month(date);

# 2)
select Category, sum(amount_paid) as Total from expense_2024 group by category;

# 3)
select Payment_mode , sum(Amount_paid) as Total_Expenses  from expense_2024 group by Payment_mode;

#4) Fuel and transportation
#Transportation
select month, sum(Amount_paid) as 'Transport Expense'
from expense_2024 
where category='Transportation'
group by month;

#Fuel
select month, sum(Amount_paid) as 'Fuel Expense'
from expense_2024 
where category='Fuel'
group by month;

#5)
select category as Category, sum(cashback) as Total_cashback  from expense_2024 group by category;

#6)
select Description,sum(Amount_Paid) as 'Amount Invested' from expense_2024 where category='Investments' group by description;

#7)
select Description as 'Mode of Transportation',sum(Amount_Paid) as 'Total Expenses' from expense_2024 where category='Transportation' group by description;

#8)
select Description as 'Food Expenses',sum(Amount_Paid) as Total from expense_2024 where category='Food' group by description;

#9)
select month as Month,  sum(Amount_paid) as 'Amount_Spent', count(description) as 'Count of hotel food' from expense_2024 where category = 'Food' group by month;

#10)
select Description,  sum(Amount_paid) as 'Loan Amount' from expense_2024 where category = 'Loans' group by description;

#11)
select Month, count(description) as 'Number of clinic visits', sum(Amount_paid) as 'Total fees' from expense_2024 where description = 'Clinic fees' group by month;

#12)
select Month, sum(Amount_paid) as 'Total expenses' from expense_2024 where Category = 'Entertainment' group by month;

#13)
select Month, count(Description) as 'Number of movies watched', sum(Amount_paid) as 'Total expenses' from expense_2024 where Description = 'Movie' group by month;

#14)
select Description, sum(Amount_paid) as 'Total expenses' from expense_2024 where category = 'Shopping' group by description;

#15)
select Month, sum(Amount_paid) as 'Total expenses' from expense_2024 where category = 'Shopping' group by month;

#16)
select Description, sum(Amount_paid) as 'Total expenses' from expense_2024 where category = 'Shopping' group by description;

#17)
select Month, sum(Amount_paid) as 'Total expenses' from expense_2024 where category = 'Shopping' group by month;




