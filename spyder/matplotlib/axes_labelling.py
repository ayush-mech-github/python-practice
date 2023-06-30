# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 21:46:13 2020

@author: AAYUSH pc
"""


#labelling the axes
#labelpad argument:for distance between axis and label
#fontdict argument:for text size and color

import matplotlib.pyplot as plt
plt.plot([2,4,6,8])
plt.xlabel("x-axis",{'size':15,'color':'red'},labelpad=20)
plt.ylabel("y-axis",{'size':15,'color':'green'},labelpad=20)
plt.show()

#size of text by keyword argument
plt.plot([2,4,6,8])
plt.xlabel("x-axis",labelpad=20,size=25,color='green')
plt.ylabel("y-axis",labelpad=20,size=25,color='red')
plt.show()
