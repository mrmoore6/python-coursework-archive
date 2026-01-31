"""
Name: Michael Moore
Date: 2/7/21
Program: web_scrap.py

This program has three functions that take in input as a txt file and counts the number of times a certain word is used\
and the average words used in a sentence.
"""


import re


def get_page(txt):
    with open(txt, mode='r', encoding='utf-8') as input_txt:
        for line in input_txt:
            print(line)


def count_word(txt, word):
    with open(txt, mode="r") as input_txt:
        count = input_txt.read()
        x = re.findall(word, count, flags=re.IGNORECASE)
        print("{}, appears {} times".format(word, len(x)))


def avg_sent(txt):
    num = 0
    with open(txt, mode='r') as input_txt:
        counter = []
        txt = input_txt.read()
        x = txt.split('.')
        for i in x:
            words = i.split()
            counter.append(len(words))
        for i in counter:
            num = num + i
        avg = num / len(counter)
        print("The average sentence length is {} words.".format(round(avg)))


# get_page('Moby_Dick_Chapter_1.txt')
count_word('Moby_Dick_Chapter_1.txt', "own")
count_word('Moby_Dick_Chapter_1.txt', "water")
avg_sent('Moby_Dick_Chapter_1.txt')
count_word('Sense_and_Sensibility_Chapter_1.txt', "own")
count_word('Sense_and_Sensibility_Chapter_1.txt', "water")
avg_sent('Sense_and_Sensibility_Chapter_1.txt')