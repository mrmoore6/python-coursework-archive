"""
Author: Michael Moore
Program: sort_and_search_list.py
Date: 10/11/20
This program accepts a list as input and sorts it then takes another value and indexes it in list.
"""
from fun_with_collections import basic_list
def get_list():
    list = basic_list.make_list()
    return list
def sort_list(list):
    list.sort()
    return list # returns sorted list parameter so it returns value when testing
def search_list(list):
    item = int(input("Enter Number"))
    if item in list:
        list = list.index(item)
        return list
    else:
        return -1

if __name__ == '__main__':
    print(sort_list(get_list()))
    print(search_list(get_list()))
