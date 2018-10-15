# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:52:57 2018

@author: 80115678
"""

import numpy as np
import pandas as pd

n= 25
solution = np.zeros(n)
solution = [np.random.randint(1,n) for x in solution]

def penalty(listt):
    summ = 0
    COUNTED = []
    for i in range(n):
        C = listt.count(listt[i])

        if listt[i] not in COUNTED:
            summ = summ + int(C*(C-1)/2)
        COUNTED.append(listt[i])

        t = listt[i]
        a = n - listt[i]
        for j in range (i+1, a+1):
            t = t + 1
            if listt[j] == t:
                summ = summ + 1

        b = listt[i] - 1
        t = listt[i]
        for j in range (i+1, b+1):
            t = t - 1
            if listt[j] == t:
                summ = summ + 1

        listt.reverse()
        t = listt[i]
        a = n - listt[i]
        
        for j in range (i+1, a+1):
            t = t + 1
            if listt[j] == t:
                summ = summ + 1
        b = listt[i] - 1
        t = listt[i]
        
        for j in range (i+1, b+1):
            t = t - 1
            if listt[j] == t:
                summ = summ + 1
        listt.reverse()
    return summ
init = solution.copy()
print(penalty(solution))
print(solution)
next_solution = [solution, penalty(solution)]
for w in range(1,21):

    neighborhood = []
    current = next_solution[1]
    ss = solution.copy()
    for i in range(n):
        ss = solution.copy()
        for j in range(1, n):
            ss[i] = j
            if penalty(ss) <= current:
                pepe = penalty(ss)
                neighborhood.append([ss, pepe])
            
    minn = penalty(solution)
    next_solution = np.zeros(n)

    for k in neighborhood:
        if k[1]<=minn:
            minn=k[1]
            next_solution = k
    solution = next_solution[0].copy()
    print("interation number {}, best fittness value: {}".format( w, next_solution[1]))
    
print(next_solution[0])
print(next_solution[1])    
