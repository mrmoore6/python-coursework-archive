"""
Name: Michael Moore
Date: 10/19/20
Program: assign_average.py
This program takes a letter grade as input selects it from dictionary and returns the value.
"""
def a():
    return "You entered A"
def b():
    return "You entered B"
def c():
    return "You entered C"
def d():
    return "You entered D"
def f():
    return "You entered F"

def switch_average(grade):
    dict = {
            "A": a(),
            "B":b(),
            "C":c(),
            "D":d(),
            "F":f()
            }
    result = dict.get(grade, "This is grade doesn't exist.")
    return result



if __name__ == '__main__':
    print(switch_average("F"))
