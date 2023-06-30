# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:05:50 2020

@author: AAYUSH pc
"""


#submatrix from matrix using slicing

import numpy

l=[[1,2,3],[4,5,6],[7,8,9]]

matrix=numpy.array(l)
print(matrix)
print()

#[row_low:row_upper,coloumn_low,coloumn_upper]
sub_mat1=matrix[0:2,0:3]
print(sub_mat1)
print()

sub_mat2=matrix[1:3,1:3]
print(sub_mat2)