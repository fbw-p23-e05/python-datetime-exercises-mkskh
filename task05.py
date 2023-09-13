# Write a Python program to convert Year/Month/Day to Day of Year using datetime module.

from datetime import datetime, timedelta

today = datetime.now()
years_day = today - datetime(today.year, 1, 1) + timedelta(days = 1)
print('Today:', today, '\nDay of the year:', years_day.days)


# print('Today:', today, '\nDay of the year:', today.strftime('%j')) result256