"""
Author: Michael Moore
Date:12/14/20
Program:Final_Project.py

This program is a health app that calculates ur bmi and logs it
into a database.


"""


class User:
    def __init__(self,f_name,l_name,age,weight,height_feet,height_inches):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.weight = weight
        self.height_inches = height_inches
        self.height_feet = height_feet

    @property
    def f_name(self):
        return self._f_name

    @f_name.setter
    def f_name(self,name):
        if name.isalpha():
            self._f_name = name
        else:
            raise TypeError("ENTER CORRECT FIRST NAME")

    @property
    def l_name(self):
        return self._l_name

    @l_name.setter
    def l_name(self, name):
        if name.isalpha():
            self._l_name = name
        else:
            raise TypeError("ENTER CORRECT LAST NAME")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0 or value > 120:
            raise ValueError("Enter Correct Value")
        else:
            self._age = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self,value):
        if not isinstance(value, float) or value < 1 or value > 1000:
            raise ValueError("Enter Correct Weight")
        else:
            self._weight = value

    @property
    def height_inches(self):
        return self._height_inches

    @height_inches.setter
    def height_inches(self, value1):
        if not isinstance(value1, int) or value1 < 1 or value1 >= 11 :
            raise ValueError("Enter Correct Inches")
        else:
            self._height_inches = value1


    @property
    def height_feet(self):
        return self._height_feet

    @height_feet.setter
    def height_feet(self,value):
        if not isinstance(value, int) or value < 1 or value > 10:
            raise ValueError("Enter Correct Feet")
        else:
            self._height_feet = value





