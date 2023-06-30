# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:49:09 2020

@author: AAYUSH pc
"""


import numpy

rows=int(input('enter no of rows'))
coloumns=int(input('enter no of coloumns'))

matrix=numpy.ndarray(shape=(rows,coloumns),dtype=int)

print('size :',matrix.size)
print('shape:',matrix.shape)
print('dimensions :',matrix.ndim)