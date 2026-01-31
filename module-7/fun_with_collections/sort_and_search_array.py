"""
Author: Michael Moore
Program: sort_and_search_array.py
Date: 10/11/20

This program sorts an array and search's through it to find inputed value.
"""
from numpy import array
def sort_array(arr):
        arr = arr.tolist()
        arr.sort()
        return arr
def search_array(num):
    try:
        number = int(input("Enter Value"))
        list = num.tolist()
        num = list.index(number)
    except ValueError:
        raise ValueError
    return num

if __name__ == '__main__':
    first_array = array([2,4,5,5,6])
    print(sort_array(first_array))
    print(search_array(first_array))


