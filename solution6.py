# -*- coding: utf-8 -*-
"""
Created on Tue May 17 11:06:34 2022

@author: kalls
"""

def formatter():
    input = open("C:\\Users\\kalls\\OneDrive\\Dokument\\EDAF05-labs-public-master\\6railwayplanning\\data\\sample\\1.in")
    numbers = input.readline().split()
    N = int(numbers[0]) #Number of nodes (cities)
    M = int(numbers[1]) #Number of edges (connections)
    C = int(numbers[2]) #Number of flow (students/soldiers)
    P = int(numbers[3]) #Number of routes
    dict1 = {}
    dict2 = {}  # We create dictionaries here
    for i in range(1, N+1):
        dict1.update({i: []})
        dict2.update({i: []})  # And fill them with keys, one for each node
    for j in range(0,M):
        edge = input.readline().split()
        dict1[edge[0]].append((edge[1],edge[2]))
        dict2[edge[1]].append((edge[0],edge[2]))
    removelist = []
    for k in range (0,P):
        removelist.append(int(input.readline()))
    for i in dict1:  # Here we combine the dictionaries into one
        if dict2[i] == []:
            continue
        elif dict1[i] == []:
            dict1[i] = dict2[i]
        else:
            # We add all edges in dict2 to the list in dict1
            for j in range(0, len(dict2[i])):
                dict1[i].append(dict2[i][j])
        
        
    return N,M,C,P,dict1,removelist


if __name__ == '__main__':
    N,M,C,P,dict,removelist = formatter()