# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:14:09 2020

@author: AAYUSH pc
"""


import numpy 

m=int(input('enter no of rows '))
n=int(input('enter no of coloumns '))

matrix=numpy.ndarray(shape=(m,n),dtype=int)

print(f'enter {m*n} elements of {m}x{n} matrix')

for i in range(m):
    for j in range(n):
        matrix[i][j]=int(input())
        
print(f'{m}x{n} matrix is :')
print(matrix)
        
