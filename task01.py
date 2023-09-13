# Write a Python script to display the various Date Time formats.
# Current date and time
# Current year
# Month of year
# Week number of the year
# Weekday of the week
# Day of year
# Day of the month
# Day of week

import datetime as dt

now = dt.datetime.now()

print(f'Current date and time: {now}')
print(f'Current year: {now.year}') # or - now.strftime('%Y') (without f string)
print('Month of year:', now.strftime('%B'))
print(f'Week number of the year: {now.isocalendar().week}') # or - now.strftime('%W') (without f string)
print(f'Weekday of the week: {now.isocalendar().weekday}') # or - now.strftime('%w') (without f string)
print('Day of year: ', now.strftime('%j'))
print('Day of the month:', now.strftime('%d'))
print('Day of week:', now.strftime('%A'))