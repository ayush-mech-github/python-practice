# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:49:11 2021

@author: AAYUSH pc
"""

#AYUSH TRIPATHI 1803240039
r1=int(input('enter no of rows of matrix A'))
c1=int(input('enter no of coloumns of matrrix A'))

A=[[0 for j in range(c1)] for i in range(r1)]

print('enter matrix elements of A')
for i in range(r1):
    for j in range(c1):
        x=int(input())
        A[i][j]=x
        
r2=int(input('enter no of rows of matrix B'))
c2=int(input('enter no of coloumns of matrix B'))

B=[[0 for j in range(c2)] for i in range(r2)]

print('enter matrix elements of B')
for i in range(r2):
    for j in range(c2):
        x=int(input())
        B[i][j]=x
        
if(c1==r2):
    P=[[0 for j in range(c2)] for i in range(r1)]
    
    for i in range(len(A)):
        for j in range(c2):
            for k in range(len(B)):
                P[i][j]+=A[i][j]*B[j][k]
                
    print('product of matrices A and B')
    for i in range(r1):
        for j in range(c2):
           print(P[i][j],end=' ')
        print()
        
else:
    print('matrix element is not possible')
    
    
    
    