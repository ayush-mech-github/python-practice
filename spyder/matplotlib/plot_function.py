# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:43:18 2020

@author: AAYUSH pc
"""


import matplotlib.pyplot as plt
plt.plot([10,20,30,40])
#for x-axis, it will take 0,1,2,3.. by default
plt.xlabel("x-axis")
plt.ylabel("y-axis")
#plt.title("plot")
plt.show()

#format argument in plot function
plt.plot([10,20,30,40],[1,2,3,4],"r",linewidth=5)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#keyword argument to change the color
plt.plot([2,4,6,8],[1,2,3,4],color='yellow',linewidth=2)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#format argument for showing points only
plt.plot([2,4,6,8],[1,2,3,4],'o')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#format argument vs keyword argument
plt.plot([1,3,5,7],[1,2,3,4],'g',color='red')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
#keyword argument has higher precedence

#two data in same plot
plt.plot([2,4,6,8],'r',[10,20,30,40],'o')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()