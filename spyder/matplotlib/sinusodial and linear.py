# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 18:03:06 2020

@author: AAYUSH pc
"""


import matplotlib.pyplot as plt
import numpy as np 

x=np.linspace(-np.pi*6,np.pi*6)
plt.plot(x,np.sin(x),color='red',label="sin(x)")
plt.plot(x,x*np.sin(2*x),color='green',label="x*sin(2*x)")
plt.plot(x,x,color='yellow',label='x')
plt.plot(x,-x,color='black',label='-x')
plt.xlabel("-6pi to 6pi")
plt.ylabel("y-axis")
plt.title("sinusodial and linear")
plt.legend()
plt.show()