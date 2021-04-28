#https://www.hackerrank.com/challenges/calendar-module/problem

import calendar
import datetime

def findDay(date):
    day_find = datetime.datetime.strptime(date, '%m %d %Y').weekday()
    return (calendar.day_name[day_find].upper())

date = input()

print(findDay(date))