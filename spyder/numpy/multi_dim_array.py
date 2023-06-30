# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:46:33 2020

@author: AAYUSH pc
"""


import numpy

arr=numpy.ndarray(shape=(3,3,3),dtype=int)

print(f'size :{arr.size}')
print(f'shape :{arr.shape}')
print(f'datatype :{arr.dtype}')
print(f'dimensions :{arr.ndim}')

val=1
x=arr.shape[0]
y=arr.shape[1]
z=arr.shape[2]

for i in range(x):
    for j in range(y):
        for k in range(z):
            arr[i][j][k]=val
            val=val+1
            
print('array elements:')
print(arr)