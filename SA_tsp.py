# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 07:23:14 2018

@author: Mah
"""
import time
import numpy as np
import math
import random
import matplotlib.pyplot as plt
def distance(x1,x2,y1,y2):
    return math.sqrt(math.pow(y2-y1,2) + math.pow(x2-x1,2))
def cost(arr,matris):
    costs=0
    for i in range(0,1655):
        if i==1654:
            costs+=matris[arr[1654]][arr[0]]
        else:
            costs+=matris[arr[i]][arr[i+1]]
                        
    return costs
def neighbour(anarray):
    aa=random.randint(0,1654)
    bb=random.randint(0,1654)
    mynewarray=anarray.copy()
    mynewarray[aa]=anarray[bb]
    mynewarray[bb]= anarray[aa]
    return mynewarray
def SA(tmax,tmin,iterations,randomresponse,xxlist,yylist):
    global matrix
    best= []
    bestx=[]
    besty=[]
    probabilities_generated=[]
    listcososher=[]
    count=0
    for i in range(iterations):
        T=tmax
        while T>tmin:
            ssss=neighbour(randomresponse)
            if cost(ssss,matrix)<cost(randomresponse,matrix):
                randomresponse=ssss
            else:
                sth=random.uniform(0,1)
                listcososher.append((cost(randomresponse,matrix), cost(ssss, matrix)))
                probabilities_generated.append((sth,np.exp((-cost(ssss,matrix)+cost(randomresponse,matrix))/T)))
                if sth<np.exp((-cost(ssss,matrix)+cost(randomresponse,matrix))/T):
                    randomresponse=ssss
                    count+=1
            print("Temperature is {} and tour cost is {}".format(T, cost(randomresponse,matrix)))
            xxlist.append(T)
            yylist.append(cost(randomresponse,matrix))
            T=0.999*T

        best.append(randomresponse)
        bestx.append(xxlist)
        besty.append(yylist)
        
    return randomresponse,cost(randomresponse,matrix),bestx,besty,best,count,probabilities_generated,listcososher
        
file = 'tsp1655.txt'
file2 = 'tsp1655.txt'
mydata = open(file, mode='r').read().splitlines()
print(mydata)
matrix= np.zeros((1655,1655))
maxx=-2222
minn = +9999999
for i in range(0, 1655):
    a= mydata[i]
    u,v,w=a.split(' ')
    u=int(u)
    v= float(v)
    w=float(w)
    for j in range(i,1655):
        b=mydata[j]
        uu,vv,ww=b.split(' ')
        uu = int(uu)
        vv= float(vv)
        ww=float(ww)
        matrix[i][j]= distance(u,uu,v,vv)
        if distance(u,uu,v,vv)<=minn:
            minn=distance(u,uu,v,vv)
        elif distance(u,uu,v,vv)>=maxx:
            maxx=distance(u,uu,v,vv)

myrandomresponse=list(np.random.permutation(np.arange(1,1655)))
first=myrandomresponse[0]
myrandomresponse.append(first)

Tmax=7500000
Tmin=0.1
iterations=1
x=[]
y=[]
mysolution, howgood,x,y,best,cc,mysomething,lll=SA(Tmax,Tmin,iterations, myrandomresponse,x,y)
xx=[]
yy=[]
for i in best:
    xx.append(i)
    yy.append(cost(i, matrix))
plt.plot(yy)
    
plt.plot(x[0])
plt.figure()
plt.plot(y[0])
print(cost(myrandomresponse,matrix))
print(howgood)
plt.figure()
plt.plot(best)

