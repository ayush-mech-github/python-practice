# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:34:52 2021

@author: AAYUSH pc
"""


#ANKIT TRIPATHI 1803240021
#solve the quadratic equation a*x**2+b*x+c=0
a=int(input('enter the value of a\n'))
b=int(input('enter the value of b\n'))
c=int(input('enter the value of c\n'))
#calculate the discriminant
d=(b**2)-(4*a*c)
#Find two solutions
sol1=(-b+(d**0.5))/(2*a)
sol2=(-b-(d**0.5))/(2*a)

print(f'the solutions are {sol1} and {sol2}')
