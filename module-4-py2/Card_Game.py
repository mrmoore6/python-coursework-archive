"""
Name: Michael Moore
Date: 2/11/2021
Program: Card_Game.py
Description: This game randomizes a 6x6 array and manipulates for each players hand and sums the total \
for winner.
"""
import numpy as np

my_array = np.arange(1, 37)
np.random.shuffle(my_array)
my_array = np.array(my_array)

my_array.resize(6, 6)
x = np.identity(6)
my_new_array = my_array * x
my_new_array = np.array(my_new_array)
id_array = np.identity(6)
c_array = np.arange(1, 37)
c_array = np.array(c_array / c_array)
c_array.resize(6, 6)
c_array = id_array - c_array
c_array = c_array * my_array
my_array = my_new_array + c_array

x = my_array.sum(axis=0)
max_score = np.max(x)
max_player = np.nanargmax(x) + 1

print(my_array)
print('\n''Results {}'.format(x))
print('\n''Winner is player {} with a {}'.format(max_player, max_score))




