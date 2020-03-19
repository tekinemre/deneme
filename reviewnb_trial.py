# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:55:33 2020

@author: EmreTekin
"""

#%%
import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3], "B": [1, 2222, 1111132323]}, index=['a', 'a', 'b'])

print(df.head())

df_ = pd.DataFrame({'x': ['abc', None, 'defss'],
                   'y': [1, 2, np.nan],
                   'z': [True, False, True]})

df_.head()


#%%
