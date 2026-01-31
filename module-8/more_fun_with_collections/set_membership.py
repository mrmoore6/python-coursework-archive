"""
Author: Michael Moore
Date: 10/16/20
Program: set_membership.py
This program takes a set and a number as input and and searchs through the set to find that number if that number...
if that number is in the set it will return turn otherwise it will return false.
"""
def in_set(set,number):
    if number in set:
        bool = True
    else:
        bool = False
    return bool



if __name__ == '__main__':
    set = {1,2,3,4,4,}
    anwser = in_set(set, 5)
    print(anwser)



