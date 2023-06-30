# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 20:53:15 2020

@author: AAYUSH pc
"""


#fontsize:
#'xx-small'   'x-small'    'small'     'medium'    'large'
#'x-large'    'xx-large'

import matplotlib.pyplot as plt
plt.plot([10,20,30,40],[90,70,50,30])
plt.xlabel("x-axis",{'size':'xx-large'})#as dictionary
plt.ylabel("y-axis",size=10)#as keyword argument
plt.show()


#color
plt.plot([10,20,30,40],[90,70,50,30])
plt.xlabel("x-axis",{'color':'green'})#as dictionary
plt.ylabel("y-axis",color='red')#as keyword argument
plt.show()

#backgroundcolor
plt.plot([10,20,30,40],[90,70,50,30])
plt.xlabel("x-axis",{'backgroundcolor':'lightblue'})#as dictionary
plt.ylabel("y-axis",backgroundcolor='yellow')#as keyword argument
plt.show()

#fontstyle or style:
#normal      italic     oblique
plt.plot([10,20,30,40],[90,70,50,30])
plt.xlabel("x-axis",{'style':'italic','color':'magenta'})#as dictionary
plt.ylabel("y-axis",fontstyle='normal',color='green')#as keyword argument
plt.show()

#fontweight or weight
#a numeric value in range 0-1000 or 'ultralight', 'light',
#'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 
#'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'
plt.plot([10,20,30,40],[90,70,50,30])
plt.xlabel("x-axis",{'fontweight':'book'})#as dictionary
plt.ylabel("y-axis",fontweight='1000')#as keyword argument
plt.show()

#fontfamily or family
#List of either names of font or 'cursive',
#'fantasy', 'monospace', 'sans', 'sans serif', 'sans-serif',
#'serif'  
plt.plot([10,20,30,40],[90,70,50,30])
plt.xlabel("x-axis",{'fontfamily':"monospace"})#as dictionary
plt.ylabel("y-axis",fontfamily='fantasy')#as keyword argument
plt.show()

