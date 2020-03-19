# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:55:33 2020

@author: EmreTekin
"""

#%%
import pandas as pd

df = pd.DataFrame({"A": [1, 2, 123123], "B": [1, 2, 12312312]}, index=['a', 'a', 'xxxxx'])

print(df.head())

#%%