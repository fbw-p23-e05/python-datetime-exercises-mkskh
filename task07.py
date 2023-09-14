import datetime as dt

# Write a Python program to select all the Sundays in a specified year.

for week in range(53):
    date = dt.datetime.strptime('2023' + str(week) + '0', '%Y%W%w')
    print(date.date())