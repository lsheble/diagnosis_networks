# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 06:14:36 2016

@author: sheble
"""
from __future__ import division

import pandas as pd
import numpy as np
import os

# same across all matrices:
day_one = np.datetime64("2007-01-01")

# to test, import one csv file:
#df = pd.read_csv('data/test_out_200/FEMALE_WHITE_46.0/FEMALE_WHITE_46.0_12.csv', header=0)

dir_perm_out = 'data/test_out_200/'
dir_perm_edges_out = 'data/test_new_perm_edges_out/'
k = 200.0

for folder_ in os.listdir(dir_perm_out):
    path = os.path.join(dir_perm_out, folder_)
    results = []
    for file_ in os.listdir(path):
        read_infile = os.path.join(path, file_)
        df = pd.read_csv(read_infile, header=0, sep=',')
        # change to date format
        df.DIAGNOSIS_DATE = pd.to_datetime(df.DIAGNOSIS_DATE, format = '%Y-%m-%d')
        df.dropna(axis=0, how='any', inplace=True)
        df['day_one'] = day_one
        df['time_test'] =(df['DIAGNOSIS_DATE']-df['day_one']) / np.timedelta64(1,'D')
        patient = df.groupby('PATIENT_KEY')
        group_list = []
        for group, items in patient:
        #    print items[[4]]
            date = np.matrix((items[[4]]))
            date = date - date.transpose()
            date = np.where(date >=0, 1, 0)
            np.fill_diagonal(date, 0)
            codes = items[[2]].values
            cols=[]
            for item in codes:
                cols.append(item[0])
            df_temp = pd.DataFrame(date)
            df_temp.columns = cols
            df_temp['source'] = codes
            df_temp = pd.melt(df_temp, id_vars=['source'], var_name='target')
            df_temp = df_temp[df_temp.value != 0]
            grouped = df_temp.groupby(['source', 'target'], as_index=False).sum() #
            if len(grouped)>0:
                group_list.append(grouped)
#            print len(group_list)
        result = pd.concat(group_list)
        result = result.groupby(['source', 'target'], as_index=False).sum()
        result['value']=result['value']/k
        results.append(result)
#        print len(results)
    out_data = pd.concat(results)
    out_data = out_data.groupby(['source', 'target'], as_index=False).sum()
    save_path = os.path.join(dir_perm_edges_out, folder_ + '.csv')
    print save_path
    out_data.to_csv(str(save_path), header=['source', 'target', 'expected'], index=False)    

# end here
