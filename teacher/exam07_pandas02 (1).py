# -*- coding: utf-8 -*-
"""exam07_pandas02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FoPLOkiOBI_N7138sMLATnMSzVUZjxp1
"""

import pandas as pd

pd.set_option('display.max_columns', 15)
pd.set_option('display.max_row', 10)

df = pd.read_csv('./datasets/auto-mpg.csv',
        names=['mpg', 'cylinders', 'displacement', 'horsepower',
               'weight', 'acceleration', 'model year', 'origin', 'name'])
df

df.head(10)

df.tail()

df.shape

df.info()

df.dtypes

df['mpg'].dtypes

print(df.mpg.dtypes)

print(df.describe())

print(df.describe().T)

df.describe(include='all')

print(df.count())


unique_value = df['name'].value_counts()

print(type(unique_value))
unique_value
print('debug01')
df['model year'].value_counts()

print(df.mean())

print(df.mpg.mean())


df.std()

# print(df.corr())
print(df)
print('debug02')
mpg_to_kpl = 0.425144
df['kpl'] = df['mpg'] * mpg_to_kpl
df.head(50)

df['kpl'] = df['kpl'].round(2)
df

df['horsepower'].unique()

import numpy as np

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')
df.info()

# df.corr()

df['origin'].unique()

df['origin'].replace({1:'USA', 2:'EU', 3:'JP'}, inplace=True)
print(df['origin'].unique())
print(df['origin'].head(30))
print(df['origin'].value_counts())

df['origin'] = df['origin'].astype('category')
print(df['origin'].dtypes)
print(df['origin'])

df['origin'] = df['origin'].astype('str')
print(df['origin'].dtypes)
print(df['origin'])

count, bin_dividers = np.histogram(df['horsepower'], bins=3)
print(count)
print(bin_dividers)

bin_names = ['저출력', '보통출력', '고출력']
df['hp_bin'] = pd.cut(x=df['horsepower'], bins=bin_dividers,
                      labels=bin_names, include_lowest=True)
df[['horsepower', 'hp_bin']].head(30)

df.info()

df1 = df[['horsepower', 'hp_bin', 'origin']]
df1

df2 = pd.get_dummies(df1)

df2

df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
                   'c2':[1, 1, 1, 2, 2],
                   'c3':[1, 1, 2, 2, 2]})
df

df_dup = df.duplicated()
df_dup

df_dup = df['c2'].duplicated()
df_dup

df2 = df.drop_duplicates()
df2

df2.info()

df2.iloc[1]

df2.loc[2]

df2.reset_index(drop=True, inplace=True)
print(df2)

