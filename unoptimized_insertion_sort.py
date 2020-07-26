# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 21:40:43 2020

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
def Insertion(a):
    '''
    Parameters
    ----------
    a : List
        Unoptimized insertion sort method 
    Returns
    -------
    None.
    '''
    N=len(a)
    for i in range(1,N):
      key = a[i]
      j = i-1
      while j >= 0 and key < a[j]:
        a[j+1] = a[j]
        j -= 1
      a[j+1] = key
      print(f"Array after iteration {i}: {a}")
a=Create_Array()      
Insertion(a)
print(f'\nSorted Array: {a}')
