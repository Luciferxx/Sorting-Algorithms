# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 21:56:27 2020

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
    Bubble sorts an array a in an optimized manner
    Returns
    -------
    None.
    '''
    N=len(a)
    for i in range(N-1):
        swapped=False
        for j in range(N-i-1):
            if a[j]>a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
                swapped=True
        print(f"Array after iteration {i+1}: {a}")             
        if swapped==False:
            break
a=Create_Array()
Bubble(a)
print('Sorted Array {}'.format(a))
