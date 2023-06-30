# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 08:05:54 2021

@author: AAYUSH pc
"""


A=[64,25,12,34,11,89,2,30,4]

for i in range(len(A)):
    min_index=i
    for j in range(i+1,len(A)):
        if A[min_index]>A[j]:
            min_index=j
    A[i],A[min_index]=A[min_index],A[i]

print('sorted array')
for i in range(len(A)):
    print(f'{A[i]}')