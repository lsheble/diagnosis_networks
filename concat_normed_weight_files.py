# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 12:54:25 2016

@author: sheble
"""

### This concatenates all of the files with observed, espected, demo values together ###
# Trying with numpy
from __future__ import print_function
import os
import glob
import pandas as pd
import numpy as np

# oe_demo = 'data/diag_edges_normed_weight_filled'
oe_demo = 'data/obs_exp_all_data'
all_files = glob.glob(os.path.join(oe_demo, '*.csv'))

np_array_list = []
for file_ in all_files:
    df = pd.read_csv(file_, index_col=None, header=0)
    np_array_list.append(df.as_matrix())

comb_np_array = np.vstack(np_array_list)
big_frame = pd.DataFrame(comb_np_array)
big_frame.columns = ['source', 'target', 'observed', 'expected', 'weight', 'gender', 'race_ethn', 'age']
big_frame = big_frame[(big_frame['observed']>5) & (big_frame['weight']>=2)]
#big_frame.columns = ['source', 'target', 'weight', 'gender', 'race_ethn', 'age']
#big_frame.to_csv('data/diag_edges_normed_weight.csv', header=True, index=False)  
big_frame.to_csv('data/diag_edges_observed_expected_weight_compressed.gzip', header=True, index=False, compression='gzip')
print('There are ' + str(len(big_frame)) + ' records in the dataframe.\n')


big_frame_5000 = big_frame[:5000]
big_frame_5000.to_csv('data/diag_edges_normed_weight_filled_5000.csv', header=True, index=False)

### End of concatenating files ###

len(big_frame)
