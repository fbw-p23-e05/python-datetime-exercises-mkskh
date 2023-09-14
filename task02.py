# Write a Python program to print the dates of yesterday, today, tomorrow.

from datetime import date, timedelta 

now = date.today()

print(f'Yesterday : {now - timedelta(days = 1)} \nToday : {now} \nTomorrow : {now + timedelta(days = 1)}')
