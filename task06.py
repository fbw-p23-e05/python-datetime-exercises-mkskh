import datetime

# Write a Python program to find the date of the first Monday of a given week.

year = '2023'
week = '37'
first_monday = '1'

date = datetime.datetime.strptime(year + week + first_monday, '%Y%W%w')

print(date.date())