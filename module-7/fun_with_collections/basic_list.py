"""
Author: Michael Moore
Program: basic_list.py
Date: 10/11/20

This program takes 3 inputs and makes them  into a list.
"""
def make_list():
    list = []
    try:

        for x in range(0, 3):
            userInput = int(get_input())
            list.insert(x, userInput)
    except ValueError:
        print("Enter Valid Values")
    return list


def get_input():
    userInput = input("Enter Value")
    return userInput

if __name__ == '__main__':
    print(make_list())

