# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 22:02:21 2020

@author: Vatsal Tulshyan
"""
def Create_Array():
    '''
    Returns
    -------
    a : LIST
        list of unsorted elements
    '''
    N = int(input('Enter number of elements: '))
    a = []
    for i in range(N):
      a.append(int(input(f'\nEnter {i+1} element: ')))
    return a
def Bubble(a):
    '''
    Parameters
    ----------
    a : List
    Bubble sorts an array a in an unoptimized manner
    Returns
    -------
    None.
    '''
    N=len(a)
    for i in range(N-1):
        for j in range(N-1):
            if a[j]>a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
        print(f"Array after iteration {i+1}: {a}")             
    
a= Create_Array()
Bubble(a)
print('Sorted Array {}'.format(a))
