# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 12:23:39 2018

@author: 80115678
"""
from math import *
import numpy as np
from math import *
    
file_name = "250cities.txt"
my_data = open(file_name)

start = 181
end = 217
least_distance = inf


def distance(a,b,c,d):
    return sqrt(pow(a-c,2)+pow(b-d,2))


my_data_row = my_data.readlines()
num_cities = int(my_data_row[0])
matrix = np.zeros((num_cities+1, num_cities+1))
di = list()
di.append(0)
disdis = np.zeros((num_cities+1))
seen = np.zeros((num_cities+1))
seen[start]=1
steps = {0:0}
masir = [start]


for i in range(2, 2798):
    a,b,c = my_data_row[i].split(' ')
    di.append([int(a),float(b),float(c)])
for i in range(1, num_cities+1):
    for j in range(1, num_cities+1):
        matrix[i][j] = distance(di[i][1],di[i][2],di[j][1],di[j][2])
        ## It's my heuristic distance!

actual_matrix = np.zeros((num_cities+1, num_cities+1))
for i in range(num_cities+1, len(my_data_row)-1):
    actual_matrix[int(di[i][0])][int(di[i][1])] = (di[i][2])
    ##It's my actual distance!
sth = True
my_closed_list=[start]
disdis = [inf for x in range(num_cities+1)]
disdis[start] = 0
while (sth):
    nonzeroind = np.nonzero(actual_matrix[start])[0]
    minn=+inf
    minn_index=0
    dfd=[]
    for i in nonzeroind:
        if disdis[i]>=disdis[start] + actual_matrix[start][i]:
            disdis[i]=disdis[start] + actual_matrix[start][i]
        if i in my_closed_list:
            continue
        dfd.append([i,disdis[start]+actual_matrix[start][i]+matrix[i][end]])
        if (disdis[start]+actual_matrix[start][i]+matrix[i][end])<minn:
            minn = disdis[start]+actual_matrix[start][i]+matrix[i][end]
            minn_index = i
        
    if minn_index not in my_closed_list:
        my_closed_list.append(minn_index)
        disdis[minn_index] = disdis[start] + actual_matrix[start][minn_index]
    else:
        while minn_index in my_closed_list:
            nonzeroind.remove(minn_index)
            dfd=[]
            for i in nonzeroind:
                if disdis[i]>=disdis[start] + actual_matrix[start][i]:
                    disdis[i]=disdis[start] + actual_matrix[start][i]
                if i in my_closed_list:
                    continue
                dfd.append([i,disdis[start]+actual_matrix[start][i]+matrix[i][end]])
                if (disdis[start]+actual_matrix[start][i]+matrix[i][end])<minn:
                    minn = disdis[start]+actual_matrix[start][i]+matrix[i][end]
                    minn_index = i
        my_closed_list.append(minn_index)
        disdis[minn_index] = disdis[start] + actual_matrix[start][minn_index]
            
            
    start = minn_index
    print(minn_index)
    if minn_index==end:
        sth = False
print(my_closed_list)
