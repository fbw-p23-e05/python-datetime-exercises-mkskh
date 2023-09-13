import datetime

year = '2023'
week = '37'
first_monday = '1'

date = datetime.datetime.strptime(year + week + first_monday, '%Y%W%w')

print(date.date())