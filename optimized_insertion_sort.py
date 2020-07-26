# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 21:52:49 2020

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
def insertion(M):
    '''
    

    Parameters
    ----------
    M : list of N elements
        Uses optimized insertion method to sort the list

    Returns Nothing
    -------
    Nothing

    '''
    for i in range(1,len(M)):
        for j in range(i):
            if M[i] < M[j]:
                M[j],M[j+1:i+1] = M[i],M[j:i]
                break
        print(f"Array after iteration {i}: {M}")
a = Create_Array()            
insertion(a)
print('Sorted Array {}'.format(a))