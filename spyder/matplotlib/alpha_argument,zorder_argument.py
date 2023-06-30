# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 19:30:59 2020

@author: AAYUSH pc
"""


#alpha-parameter determining transparency of the line
#it lies between 0 to 1

import matplotlib.pyplot as plt
plt.plot([10,20,30,40],[90,80,70,60],alpha=0.9)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("alpha")
plt.show()

#zorder-if two curves overlap, it is used to decide which curve will be
#overshown
plt.plot([10,20,40,50],zorder=1)
plt.plot([10,20,70,80],zorder=2)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("zorder")
plt.show()

plt.plot([0,0],[-1,1],zorder=3,linewidth=20)
plt.plot([-1,1],[1,-1],zorder=2,linewidth=20)
plt.plot([-1,1],[-1,1],zorder=1,linewidth=20)