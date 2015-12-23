# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 18:02:51 2015

@author: kmajumdar
"""

''' Modified Line Length '''

import numpy as np
def mll(signal,window):
    arr = []
    for i in range(0,len(signal)-window,window):
        temp = signal[i:i+window]
        grad = np.gradient(temp)
        abso = []
        for j in grad:
         abso.append(np.abs(j))
        arr.append(np.mean(abso)) 
        
    return arr

    