# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 14:54:26 2016

@author: ShebleAdmin
"""

### PERMUTATIONS!!! ###
### Start: test getting observed edges for each demographic file    
import os
import numpy as np
import pandas as pd


dir_name = 'users/sheble/data/patient_diag_groups/'
dir_perm_out =  'users/sheble/data/test_out/'

def shuffle_col2(df,column):
    df=df.copy()
    selected = list(df[column].values)
    np.random.shuffle(selected)
    df[column] = selected
    return df
    

for infile in os.listdir(dir_name):
    read_infile = os.path.join(dir_name, infile)
    xtra_dir = str(infile).rstrip('.csv') + '/'
    mkdir_path = os.path.join(dir_perm_out, xtra_dir)
    os.mkdir(mkdir_path)
    df_to_perm = pd.read_csv(read_infile, header=0, sep=',', usecols=['PATIENT_KEY', 'DIAGNOSIS_DATE', 'DIAGNOSIS_CODE'])
    i = 0
    while i < 200:
        df_to_perm['PATIENT_KEY'] = shuffle_col2(df_to_perm,'PATIENT_KEY')
        out_file = str(infile).rstrip('.csv') + '_' + str(i) + '.csv'
        save_path = os.path.join(dir_perm_out, xtra_dir, out_file)
        df_to_perm.to_csv(str(save_path), header=True, index=False) #index_label='index'
        i = i + 1
