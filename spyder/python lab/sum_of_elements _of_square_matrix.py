# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:13:27 2021

@author: AAYUSH pc
"""


#ANKIT TRIPATHI 1803240021
import numpy as np
m=int(input('enter no of rows'))
n=int(input('enter no of coloumns'))
matrix=np.ndarray(shape=(m,n),dtype=int)
s=0
print('enter elements of matrix')#3*3 matrix
for i in range(m):
    for j in range(n):
        matrix[i][j]=int(input())
        s=s+matrix[i][j]
print(f'sum of elements is {s}')
