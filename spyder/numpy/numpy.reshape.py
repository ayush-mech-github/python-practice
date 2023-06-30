# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:18:43 2020

@author: AAYUSH pc
"""


import numpy

l=[1,2,3,4,5,6]
arr=numpy.array(l)

print('size :',arr.size)
print('dimensions :',arr.ndim)
print('datatype :',arr.dtype)
print('shape',arr.shape)

new_arr=arr.reshape(2,3)
print(new_arr)
print('dimensions :',new_arr.ndim)
print('shape :',new_arr.shape)