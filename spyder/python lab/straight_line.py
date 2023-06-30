# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:12:22 2021

@author: AAYUSH pc
"""


#AYUSH TRIPATHI 1803240039
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-5,5,100)
y=2*x+1
plt.plot(x,y,label='y=2*x+1')
plt.title('graph of y=2*x+1')
plt.xlabel('x')
plt.ylabel('y')
plt.show()