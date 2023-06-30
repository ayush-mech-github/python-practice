# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:00:23 2020

@author: AAYUSH pc
"""


import numpy as np

l=[[1,2,3],[4,5,6],[7,8,9]]

matrix=np.array(l)

for i in matrix:
    for j in i:
        print(j,end=' ')
        print()