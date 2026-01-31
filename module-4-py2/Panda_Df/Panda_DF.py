"""
Name: Michael Moore
Date: 2/13/21
Program: Panda_DF.py

This program uses pandas to set-up and manipulate a dataframe.
"""
import pandas as pd
from numpy import mean

def c(x):
    x = (x - 32) * 5 / 9
    return round(x)


user_data = pd.read_csv('Days of week.txt', sep='|', index_col='INDEX')
print(round(user_data.mean(), 3))
print('\n', user_data.std())
print('\n', user_data.max(numeric_only=True))

user_new_data = pd.read_csv('Weather.txt', sep='|', index_col='INDEX')

new_user_data = pd.merge(user_data, user_new_data)
new_user_data.set_index('Day of week')
new_user_data['Max Temp'] = new_user_data['Max Temp'].apply(c)
new_user_data['Min Temp'] = new_user_data['Min Temp'].apply(c)
z = new_user_data[["Max Temp"]].values.tolist()
y = new_user_data[["Min Temp"]].values.tolist()
i = [mean(i) for i in zip(z, y)]
new_user_data.insert(5, "Avg Temp", i)
x = new_user_data.reindex(['Day of week', 'Max Temp', 'Min Temp', 'Avg Temp', 'Precip', 'New Snow'], axis="columns")
x.set_index('Day of week')
print('\n', x)


