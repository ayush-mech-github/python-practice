# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 17:31:26 2020

@author: AAYUSH pc
"""


import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-np.pi*2,np.pi*2)

plt.plot(x,np.sin(x),color='red',label="sin(x)")
plt.plot(x,np.cos(x),color='green',label="cos(x)")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("sine and cosine graphs")
plt.legend()
plt.show()
