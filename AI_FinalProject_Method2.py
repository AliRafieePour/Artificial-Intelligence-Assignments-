# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 02:07:53 2019

@author: Mah
"""
import random
import numpy as np
import matplotlib.pyplot as plt

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


def initial_populat(l, w, d):
    t = True
    mylist= []
    while t:
        mylist.append(list(np.random.permutation(np.random.permutation(list(np.ones(w)) + list(np.zeros(l-w))))))
        mylist.append(list(np.random.permutation(np.random.permutation(list(np.ones(w)) + list(np.zeros(l-w))))))
        print(fittness(mylist, d))
        if fittness(mylist, d)==2:
            break
        else:
            mylist= []
    return mylist



def opt(pop):
    return pop*(pop-1)



def neigh(init):
    init0 = init.copy()
    ne = []
    for i in range(len(init)):
        for j in range(len(init)):
            if i != j:
                c = init[i]
                init[i]=init[j]
                init[j] = c
                ne.append(init)
                init = init0.copy()
    return ne

def check(ne, add, d):
    ne.append(add)
    return fittness(ne, d)

   
def sa(first ,init, d, l, t):
    max= -8888
    fi = []
    for i in range(5000):
        c = 0
        while(t>0.001):
            c = c + 1
            hamsa = neigh(init)
            rand = random.choice(hamsa)
#            if check(first, init, d)==opt(len(first)):
#                first.append(init)
#                return first
            if check(first, init, d)<=check(first, rand, d):
                first.remove(init)
                first.remove(rand)
                init = rand.copy()
                t = random.uniform(0.9,0.99999)*t
            elif check(first, init, d)>check(first, rand, d):
                first.remove(init)
                first.remove(rand)
                if random.uniform(0, 1)<np.exp((check(first, rand, d) - check(first, init, d))/t):
                    init = rand.copy()
                    t = random.uniform(0.9,0.99999)*t
        t = random.uniform(80,150)
        first.append(list(init))
        if fittness(first, d)==opt(len(first)):
            return first
        else:
            if max<=fittness(first, d):
                max = fittness(first, d)
                fi = init.copy()
            first.remove(list(init))
    first.append(list(fi))
    return first
            

def solve(l, w, d):
    first = initial_populat(l, w, d)
    final = []
    cc = 2
    while (first != []):
        print('*')
        cc = cc + 1
        mylist = list(np.random.permutation(np.random.permutation(list(np.ones(W)) + list(np.zeros(L-W)))))  
        first = sa(first, mylist, d, l, random.uniform(80,180))
        print(first)
        if first != []:
            print('*******{}*******{}*******len={}'.format(cc, fittness(first, d), len(first)))
            final = first.copy()
    print('^^^')
    return final
        
L, W, D= 18, 8, 8
print(solve(L, W, D))
