# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 12:04:13 2016

@author: sheble

### THIS MERGES OBSERVED ('occurs') AND EXPECTED VALUES FOR EACH DEMO GROUP

"""
from __future__ import print_function
import os
import pandas as pd


observed = 'data/co_diag_observed_minmax_data'
expected_values = 'data/regroup_permuted_edges'
oe_demo = 'data/obs_exp_all_data'

for file_ in os.listdir(observed):
    p1 = os.path.join(observed, file_)
    p2 = os.path.join(expected_values, file_)
    df1 = pd.read_csv(p1, header=0, usecols=['source', 'target', 'occurs'])
    df2 = pd.read_csv(p2, header=0)
    df2.columns=['target', 'source', 'expected']
    df2.target = df2.target.astype(str)
    df2.source = df2.source.astype(str)
    df1.target = df1.target.astype(str)
    df1.source = df1.source.astype(str)
    df1 = pd.merge(df1, df2, how='left', on=['source', 'target'])
    # fill_value = df1['expected'].min(): this is generally 0.005 since 200 permutations were run...
    # print(fill_value)
#    df1['expected'] = df1['expected'].fillna(0.005)
    dlist = file_.split('_')
    df1['gender']=dlist[0]
    df1['race_ethn']=dlist[1]
    dlist[2]=dlist[2].strip('.csv')
#    df1['age']=float(dlist[2])
    df1['age']=dlist[2]
#    df1['weight']=((df1['occurs']-df1['expected'])*(df1['occurs']-df1['expected']))/df1['expected']
    df1['weight'] = (df1['occurs']/df1['expected'])
    df1 = df1[['source', 'target', 'occurs', 'expected', 'weight', 'gender', 'race_ethn', 'age']]
    save_path = os.path.join(oe_demo, file_)
    df1.to_csv(str(save_path), header=True, index=False)
