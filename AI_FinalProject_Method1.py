# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 02:07:53 2019

@author: Mah
"""
import random
import numpy as np
import matplotlib.pyplot as plt
def populate(pop, length, weight):
    mypopulation =[list(np.random.permutation(np.random.permutation(list(np.ones(weight)) + list(np.zeros(length-weight))))) for i in range (pop)]
    return mypopulation    
#take elemnts of the problem

def fittness(pop, d):
    count = 0
    nomreh=0
    for element1 in pop:
        for element2 in pop:
            count=0
            for i in range(len(element1)):
                if element1[i]!=element2[i]:
                    count+=1
            if count>=d:
                nomreh+=1
    return nomreh

def flip(arr):
    if arr:
        return 0
    else:
        return 1
    
def neighbours(pop, mypop, l ,d):
    neigh = []
    for i in range(pop):
        mypopcopy = mypop.copy()
        mycopy=mypop[i].copy()
        mycopy2=mypop[i].copy()
        for j in range(l):
            for k in range(j+1, l):
                c = mycopy2[j]
                mycopy2[j] = mycopy2[k]
                mycopy2[k] = c
                mypop[i] = mycopy2
                neigh.append(mypop)
                mycopy2 = mycopy.copy()
                mypop=mypopcopy.copy()
    summ=0
    for n in range(len(neigh)):
        summ+=fittness(neigh[n], d)
    return neigh

def sa(t, init, pop, l, d):
    y=[]
    print('Initial fittness={}'.format(fittness(init, d)))
    while t>0.001:
        y.append(fittness(init, d))
        neighborhood = neighbours(pop, init, l, d)
        arandomresponse = random.choice(neighborhood)
        aa = fittness(arandomresponse, d)
        bb = fittness(init, d)
        print('aa={}, b={}'.format(aa, bb))
        if (aa<bb):
            if random.uniform(0,1)<np.exp((aa-bb)/t):
                print(' Worsening Step')
                print('{}  {}'.format(bb, aa))
                init = arandomresponse.copy()
                print('Next move= {}'.format(aa))
                print('************************************')
                t = 0.95*t
        elif (aa==bb):
            if random.uniform(0,1)<0.2:
                print(' Moving around in Plateux')
                init = arandomresponse.copy()
                print('Next move= {}'.format(aa))
                print('************************************')
                t = 0.95*t
            else:
                continue
        elif (aa>bb):
            print('Improving Step')
            print('{}  {}'.format(bb, aa))
            init = arandomresponse.copy()
            print('Next move= {}'.format(aa))
            print('************************************')
            t = 0.95*t
        if y.__contains__(pop*(pop-1)):
            return y, init
    return y, init

L, W, D= 18, 8, 8
population = 15
mypop = populate(population, L, W)
y, ini = sa(50, mypop, population, L, D)
plt.plot(y)