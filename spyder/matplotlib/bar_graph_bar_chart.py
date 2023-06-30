# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 09:01:39 2021

@author: AAYUSH pc
"""


import matplotlib.pyplot as plt

#bar(x,height,width=0.8,bottom=none,align='centre',data=None,**kwargs)
x=['science','commerce','arts']
h=[80,50,40]#no of students enrolled
c=['red','magenta','purple']#color of each bar
plt.bar(x,h,width=0.2,color=c)
plt.xlabel("courses")
plt.ylabel("Students enrolled")
plt.title('Students enrolled for different courses in 2021")
plt.show()