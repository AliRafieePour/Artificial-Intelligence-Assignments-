# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:06:47 2018

@author: Mah
"""
import random
import numpy as np
import math
import matplotlib.pyplot as plt
import time
numofgenerations = 50
mygeneration = []
mygene_fitness = []
def flip(a):
    if a==0:
        return 1
    else:
        return 0
def makefirstgeneration():
    global clauses
    for i in range(numofgenerations):
        sth_toadd=[np.random.choice([0, 1], replace=True) for x in range(435)]
        mygeneration.append(sth_toadd)
        mygene_fitness.append(fittness(clauses,sth_toadd))
    summ= sum(mygene_fitness)
    mygene_prob=[i/summ for i in mygene_fitness]
    return mygeneration,mygene_fitness,mygene_prob
def fittness(anarray,aresponse):
    countt=0
    for v in anarray:
        temp_sat=0
        for k in v:
            if k>=0 and aresponse[k-1]:
                temp_sat=1
            elif k<0 and aresponse[-k-1]==0:
                temp_sat=1
        if temp_sat==1:
            countt+=1
    return countt
def makeoffspring(a_prob,b_list):
    newgeneration = []
    for i in range(25):
        first = random.choices(b_list,a_prob)[0]
        second= random.choices(b_list,a_prob)[0]
        ran=np.random.choice([0,1])
        if ran==0:
            a=random.randint(0,434)
            b=random.randint(0,434)        
            if a>=b:    
                first_middle=first[b:a]
                second_middle=second[b:a]
                first[b:a]=second_middle
                second[b:a]=first_middle
                newgeneration.append(first)
                newgeneration.append(second)
            else:
                first_middle=first[a:b]
                second_middle=second[a:b]
                first[a:b]=second_middle
                second[a:b]=first_middle
                newgeneration.append(first)
                newgeneration.append(second)
        elif ran==1:
            third=random.randint(0,434)
            third1=first[0:third]
            third2=second[0:third]
            first[0:third]=third2
            second[0:third]=third1
            newgeneration.append(first)
            newgeneration.append(second)
            

    for i in range(random.randint(1, 5+int(0.02*len(a_prob)))):
        aa=random.randint(0,49)
        for kk in range(random.randint(100,200)):
            dd=random.randint(0,434)
            try:
                uu=newgeneration[aa]
            except:
                print('aa={}'.format(aa))
                print(len(newgeneration))
            try:
                uu[dd]=flip(uu[dd])
            except:
                print('dd={}'.format(dd))
                    
            newgeneration[aa]=uu
        
    return newgeneration   

file = 'sat1027.txt'
mydata= open(file, mode='r').read().splitlines()
clauses = []
for l in mydata:
    sth=l.split('\t')
    alist=[]
    for m in sth:
        if m!='0':
            alist.append(int(m))
    clauses.append(alist)

a,b,c=makefirstgeneration()
jok= sum(c)
c= [x/jok for x in c]
neww = makeoffspring(c,a)

neww2=[fittness(clauses,x) for x in neww]
summ=sum(neww2)
neww2 = [x/summ for x in neww2]
maxes = []
mines = []
for i in range(100):
    neww=makeoffspring(neww2, neww)+neww
    neww2=[fittness(clauses,x) for x in neww]
    maxes.append(max(neww2))
    mines.append(min(neww2))
    jjok=sum(neww2)
    neww2=[x/jjok for x in neww2]

plt.plot(maxes,color='blue')
#plt.plot(mines,color='red')

