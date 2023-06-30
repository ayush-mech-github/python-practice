# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:57:56 2020

@author: AAYUSH pc
"""


import numpy

l=[1,2,3,4]
arr=numpy.array(l)
 
print(arr)
print('size :',arr.size)
print('datatype :',arr.dtype)
print('dimensions :',arr.ndim)
print('shape :',arr.shape)

l=[[1,2,3],[4,5,6],[7,8,9]]
matrix=numpy.array(l)
 
print(matrix)
print('size :',matrix.size)
print('datatype :',matrix.dtype)
print('dimensions :',matrix.ndim)
print('shape :',matrix.shape)
#it is faster than lists in python
#this is because it has binding with c