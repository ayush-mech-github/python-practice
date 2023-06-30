# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:34:50 2020

@author: AAYUSH pc
"""


#creating 1D array
import numpy

n=int(input('enter the size of array:'))
arr=numpy.ndarray(shape=(n),dtype=int)

print('enter %d elements:'%n)

for i in range(n):
    arr[i]=int(input())
    
print(arr)
