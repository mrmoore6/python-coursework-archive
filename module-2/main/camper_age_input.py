"""
Program: camper_age_input.py
Author: Michael Moore
Last date modified: 9/5/2020

  The purpose of this program is to convert years into months.
"""
from main import constants


def convert_to_months(year):
    months = year * constants.MONTHS
    return(months)


if __name__ == '__main__':
    age_in_years = int(input("Enter years"))
    age_in_months = convert_to_months(age_in_years)
    print("{} Year is {} months".format(age_in_years, age_in_months))



#FFF
