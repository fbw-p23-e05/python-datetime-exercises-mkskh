import datetime as dt

for week in range(53):
    date = dt.datetime.strptime('2023' + str(week) + '0', '%Y%W%w')
    print(date.date())