# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:13:08 2020

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
def linear_Search(a,x):
    '''
    

    Parameters
    ----------
    a : List
        List in which element needs to be searched
    x : List
        element that needs to searched

    Returns
    -------
    None.

    '''
    flag = False
    for i in a:
        if x==i:
            print('Found')
            flag = True
            break
        else:
            continue
    if flag==False:
        print('Not found')
    
a=Create_Array()
x=int(input('Enter the Element that needs to be searched'))
linear_Search(a,x) 
   
