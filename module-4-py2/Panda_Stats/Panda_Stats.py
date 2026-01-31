"""
Name: Michael Moore
Date: 2/14/2021
Program: Panda_Stats.py

Uses different built-in functions to manipulate a lot of data.
"""
import pandas as pd

df = pd.read_csv('ign.csv', sep=',')

print(df.shape)
df.drop("Unnamed: 0", axis=1, inplace=True)
print("\n", df.loc[:, 'title'])
print("\n", df.loc[:, 'genre'])
print("\n", df.loc[:, 'release_year'])
print("\n", round(df['score'].mean(), 2))
print("\n", df['score'].max())
print("\n", round(df['score'].std(), 2))
df['score'] = df['score'].multiply(10)
high_scores_bool = df['score'] > df['score'].mean()
high_scores = df[high_scores_bool]
print('\n', high_scores)
ser = pd.Series(high_scores['platform'])
print("\n", ser.value_counts(ascending=False))
