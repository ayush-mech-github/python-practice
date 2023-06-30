# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 09:12:40 2021

@author: AAYUSH pc
"""


def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
            
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return(i+1)

def quick_sort(arr,low,high):
    if len(arr)==1:
        return arr
    if low<=high:
        pi=partition(arr,low,high)
        quick_sort(arr,low,(pi-1))
        quick_sort(arr,pi+1,high)

arr=[39,49,28,3,11,22,63,45,12]
n=len(arr)
quick_sort(arr,0,n-1)
print('sorted array is')
for i in range(n):
    print(f'{arr[i]}')
        
        
        
        
        
        
        
        