# 21. Write a Python program to convert a date or yyyy-mm-dd format to dd-mm-yyyy

import datetime
today_date = datetime.date.today()
print('Todays date: ', today_date)

print('Formatted date is :  ',today_date.strftime("%d-%m-%Y"))   # 05-01-2023

# print('Formatted date is :  ',today_date.strftime("%d-%m-%y"))   # 05-01-23
# print('Formatted date is :  ',today_date.strftime("%D"))   # 01/05/23
# print('Formatted date is :  ',today_date.strftime("%t"))   # 01/05/23

