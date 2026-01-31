"""
Author: Michael Moore
Program: basic_list_exception.py
Date: 10/11/20

This program is a modified verison of basic list that checks to see if input is between 0 and 50 before running
"""
def make_list():
    list = []
    try:

        for x in range(0, 3):
            userInput = int(get_input())
            if userInput < 50 and userInput > 0:
                list.insert(x, userInput)
            else:
                raise ValueError

    except ValueError:
        raise ValueError
    return list


def get_input():
    userInput = input("Enter Value")
    return userInput

if __name__ == '__main__':
    print(make_list())

