# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 09:35:39 2021

@author: AAYUSH pc
"""


import matplotlib.pyplot as plt

#barh(y,width,height=0.8,left=None,align='centre',**kwargs)
y=['ECE','ME','CSE','EE','ECE']
w=[380,490,450,540,430]
c=['red','purple','orange','blue','magenta']
plt.barh(y,width=w,height=0.2,color=c)
plt.xlabel('Engineering courses')
plt.ylabel("No of students enrolled")
plt.title('ABES-EC students enrolled')
plt.show()