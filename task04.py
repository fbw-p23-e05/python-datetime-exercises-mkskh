# Write a Python program to print the next 5 days starting today.

from datetime import datetime, timedelta

today = datetime.now()
print('Today:', today, '\nNext 5 days:')

for i in range(1,6):
    print(today + timedelta(days = i))