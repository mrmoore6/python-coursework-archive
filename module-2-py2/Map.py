"""
Name: Michael Moore
Date: 2/1/21
Program: Map.py
This program takes a list of strings and maps to a function that outputs the length of each saves that data back into
a list. """


def string_list(word):
    count = len(word)
    count_list = [word, count]
    return count_list


a_list =["Hi", "My", "Name", "Is", "Michael", "And", "This", "Is", "My", "List"]
hey = list(map(string_list, a_list))
print(hey)
my_list = []
for i in a_list:
    my_list.append(len(i))
    if len(my_list) == len(a_list):
        print(my_list)




