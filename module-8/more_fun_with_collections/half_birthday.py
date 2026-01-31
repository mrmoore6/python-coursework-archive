"""
Name: Michael Moore
Date: 10/17/20
Program: half_birthday.py
This program takes a birthday as input as converts it to a half birthday.
"""
from datetime import datetime, timedelta,date
TIME_NOW = datetime.now()
def half_birthday(datetime):
    half_b_day = datetime + timedelta(days= 182.5)
    return "Your half b-day is {}".format(half_b_day)
if __name__ == '__main__':
    birthday = datetime(2020,12,31)
    print(half_birthday(birthday))
