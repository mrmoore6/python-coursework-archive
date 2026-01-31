"""
Name: Michael Moore
Date: 1/3/21
Program: regex.py

This program uses regex to sort through a phrase.
"""
import re

txt = "I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face " \
      "my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye " \
      "to see its path. Where the fear has gone there will be nothing. Only I will remain.– Frank Herbert, Dune "

x = re.findall("[a-z]*f", txt, flags=re.IGNORECASE)
print(len(x))
x = re.findall("f", txt, flags=re.IGNORECASE)
print(len(x))
x = re.findall("not", txt)
print(len(x))
x = re.sub("I", "You", txt)
y = re.sub("my", "your", x)
z = re.sub("me", "you", y)
print(z)


