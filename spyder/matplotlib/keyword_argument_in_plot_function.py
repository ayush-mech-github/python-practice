# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:27:36 2020

@author: AAYUSH pc
"""


import matplotlib.pyplot as plt

#linewidth:to change the width of line
plt.plot([1,2,3,4],linewidth=2)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#antialiased:smoothen the line of the plot
plt.plot([10,20,30,40],antialiased=False)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#color or c:to change the color of the plot
import numpy as np
arr=np.arange(0,5)
plt.plot(arr**2,marker="D",color='yellow',linewidth='2')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#dashes:to change the style of line
plt.plot([2,4,6,8],[1,3,5,7],dashes=[2,8],)#dashes=[length,space]
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#linestyle or ls:to change line style
plt.plot([9,18,27,36],linestyle="-.")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#markeredgecolor:to change the color of the marker edge
plt.plot([10,8,6,4],[4,6,8,10],marker='H',markeredgecolor='red')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#markeredgewidth:to change the width of the marker
plt.plot([20,40,60,80],[80,60,40,20],marker='x',markeredgewidth=10)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#markerfacecolor
plt.plot([6,12,18,24],[2,4,6,8],marker='o',markerfacecolor='k')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()