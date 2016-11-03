# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 00:41:22 2016

@author: ShebleAdmin

check the first two age categories: how is this going to work? (1 inclusive or exclusive for each)
"""

import pandas as pd

# df = pd.read_csv('data_20160705/edges_asian_gt2_times_expected.csv')

df = pd.read_csv('/Users/ShebleAdmin/Documents/emr_accessible/diag_edges_observed_expected_weight_compressed')

df.head()
df['age']=df['age'].str.replace('0-to-12mo', '0-to-1')
df['age']=df['age'].str.replace('90-and-up', '90-to-115')
df['age'].unique()

df_age = pd.DataFrame(df['age'].str.split('-').tolist(), columns=['age_lower', 'to', 'age_upper'])
df=df.join(df_age)
df.head()

age_values = pd.crosstab(df.age, [df.age_lower, df.age_upper], rownames=['age'], colnames=['age_lower', 'age_upper'])

df['weight']=df['weight'].round(3)
df['expected']=df['expected'].round(3)
df.columns
df = df[['source', 'target', 'observed', 'expected', 'weight', 'gender', 'race_ethn', 'age', 'age_lower', 'age_upper']]
df.head()

df.to_csv('/Users/ShebleAdmin/Documents/emr_accessible/diag_edges_observed_expected_weight_20161103.txt', index=False, header=False, sep='\t')
