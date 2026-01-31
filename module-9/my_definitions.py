"""
Author: Michael Moore
Date: 10/25/20
This program declares for funtions one that prints a greeting one that prints a name, one that prints a dictionary and one...
prints a set.
"""
def greeting():
    print("Hello There")

def author(name):
    print('{}: {}'.format("Author",name))

def print_dict(dict):
    for key,values in dict.items():
        print(key,values)

def print_set(set):
    for i in set:
        print(i)

