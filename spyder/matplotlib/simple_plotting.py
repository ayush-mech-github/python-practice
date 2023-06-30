# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:19:04 2020

@author: AAYUSH pc
"""


#matplotlib is a library in python used to plot graph of given data
import matplotlib
matplotlib.__version__
#a figure can contain 1 or more than 1 axes
#whatever we see on the figure is called artist

#pyplot is a module in matplotlib package which provides simple functions..
#to add plot elements like line, image, text etc. to the current axes in
#the current figure.

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[5,6,7,8])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("first plot")
plt.show()