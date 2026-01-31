"""
Author: Michael Moore
Date: 10/17/20
Program: dict_membership.py
This program take a dictionary and a number as a input and checks to see if that value is in the dictionary and returns..
true or false to the main program.
"""

def in_dict(value, dict):
    bool = True
    for i in dict:
        if value in i:
            bool = True
        else:
            bool = False
    return "{}, {}".format(bool, dict)


if __name__ == '__main__':
    test_dict = {"A:50", "B:60", "C:40", "D:60"}
    test = in_dict("50", test_dict)
    print(test)
