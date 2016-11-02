# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 00:41:22 2016

@author: ShebleAdmin
"""

import pandas as pd

df = pd.read_csv('data_20160705/edges_asian_gt2_times_expected.csv')
df.head()
df['age']=df['age'].str.replace('0-to-12mo', '0-to-1')
df['age']=df['age'].str.replace('90-and-up', '90-to-115')
df['age'].unique()

df_age = pd.DataFrame(df['age'].str.split('-').tolist(), columns=['age_lower', 'to', 'age_upper'])
df=df.join(df_age)
df.head()

pd.crosstab(df.age, [df.age_lower, df.age_upper], rownames=['age'], colnames=['age_lower', 'age_upper'])

df['weight']=df['weight'].round(3)

df = df[['source', 'target', 'weight', 'gender', 'race_ethn', 'age', 'age_lower', 'age_upper']]
df.head()

df.to_csv('data_20160705/edges_asian_gt2_times_expected_20160707.txt', index=False, header=False, sep='\t')

