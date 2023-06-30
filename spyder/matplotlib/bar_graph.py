# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 09:24:41 2021

@author: AAYUSH pc
"""


import matplotlib.pyplot as plt

x=['CSE','ME','ECE','EE','IT']
h=[650,600,730,810,780] 
c=['red','purple','orange','blue','magenta']
plt.bar(x,h,color=c,width=0.2)
plt.xlabel('Engineering courses')
plt.ylabel("No of students enrolled")
plt.title('ABES-EC students enrolled')
plt.show()