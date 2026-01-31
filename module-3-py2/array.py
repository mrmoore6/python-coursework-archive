"""
Name: Michael Moore
Date: 2/9/21
Program: array.py

This program uses numpy array and uses different built-in functions to manipulate it.
"""

import numpy as np
my_first_array = np.array([[10, 15, 20], [2, 3, 4], [9, 14.5, 18]])
my_second_array = np.array([[1, 2, 5], [8, 0, 12], [11, 3, 0]])
print("\n", my_first_array)
print("\n", my_second_array)
print("\n", my_first_array.shape)
print("\n", my_first_array[0:2, 0:2])
my_array_even = my_first_array % 2 == 0
print("\n", my_array_even)
array_add = np.add(my_first_array, my_second_array)
print("\n",  array_add)
array_multi = np.multiply(my_first_array, my_second_array)
print("\n", array_multi)
print("\n", my_second_array.sum())
print("\n", np.product(my_second_array))
print("\n", my_second_array.max())
print("\n", my_second_array.min())