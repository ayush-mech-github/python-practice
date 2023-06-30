# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:12:27 2020

@author: AAYUSH pc
"""


r1=int(input('enter no of rows of matrix A'))
c1=int(input('enter no of coloumns of matrix A'))

#initialize matrix A
A=[[0 for j in range(c1)] for i in range(r1)]

#input matrix A
print('enter matrix elements of A')
for i in range(r1):
    for j in range(c1):
        x=int(input())
        A[i][j]=x
        
r2=int(input('enter no of rows of matrix B'))
c2=int(input('enter no of coloumns of matrix B'))

#initialize matrix B
B=[[0 for j in range(c2)] for i in range(r2)]

#input matrix B
print('enter matrix elements of B')
for i in range(r2):
    for j in range(c2):
        x=int(input())
        B[i][j]=x
        
#if no of coloumns of matrix A is equal to no of rows
#of matrix B
if(c1==r2):
    #initialize product matrix
    P=[[0 for j in range(c2)] for i in range(r1)]
    for i in range(len(A)):
        for j in range(c2):
            for k in range(len(B)):
                P[i][j]+=A[i][k]*B[k][j]

    #print the product matrix
    print('product of matrices A and B')
    for i in range(r1):
        for j in range(c2):
            print(P[i][j],end=' ')
        print()   
        
else:
    print('matrix multiplication is not possible')
    
    
  
    
            
    

