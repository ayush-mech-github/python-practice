# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 09:29:02 2021

@author: AAYUSH pc
"""


#AYUSH TRIPATHI 1803240039
def remove(l):
    final_l=[]
    for num in l:
        if num not in final_l:
            final_l.append(num)
    return final_l

l=[1,2,3,4,3,2,6,7,8]
print(remove(l))
