"""
Name: Michael Moore
Date: 2/9/21
Program: array_manipulation.py

This program uses a series of built-in functions to manipulate an array.
"""
import numpy as np

my_array = np.array([[1, 2, 5], [8, 0, -7], [7, 3, 9]])
print(my_array)
new_array = my_array.transpose()
print('\n', new_array)
new_array = new_array.swapaxes(0, 1)
print('\n', new_array)
new_array = np.flip(new_array, 1)
print('\n', new_array)
new_array = np.append(new_array, [[3, 4, 5]], axis=0)
new_array2 = np.array([[7], [8], [9], [0]])
np.append(new_array, new_array2, axis=1)
new_array = np.append(new_array, new_array2, axis=1)
print('\n', new_array)
new_array = np.delete(new_array, 3, 1)
print("\n", new_array)
new_array = np.array(new_array)
new_array.resize(6, 2)
print('\n', new_array)
new_array2 = np.split(new_array, 3)
new_array2 = np.array(new_array2)
print('\n', new_array2[1:2])
new_array3 = new_array2[2:3]
new_array3 = np.array(new_array3)
new_array3 = new_array3.flatten()
print('\n', new_array3)
