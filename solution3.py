# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 10:24:01 2022

@author: kalls
"""
 #\
def formatter():
    input = open("C:\\Users\\kalls\\OneDrive\\Dokument\\EDAF05-labs-public-master\\3makingfriends\\data\\secret\\1small.in")
    firstline = input.readline()
    space = firstline.find(" ")
    N = int(firstline[:space])
    M = int(firstline[space:])
    pairs = []
    weights = []
    for i in range(0,M):
        line = input.readline().replace("\n","")
        space1 = line.find(" ")
        space2 = line.find(" ",space1+1)
        person1 = int(line[:space1])
        person2 = int(line[space1:space2])
        weight = int(line[space2:])
        pairs.append([person1,person2])
        weights.append(weight)
    return N,M,pairs,weights
        
def people(N,M,pairs,weights): #Dictionary av dictionary (coolt)
    dict = {} #Key är en person, value är en dictionary för alla dess vänner
    # Inre dictionary för varje vän: key är vän value är viken av vänskapen 
    for i in range(1,N+1):
        dict.update({i:{}}) 
        for idx,p in enumerate(pairs):
            
            if (p[0] == i):
                dict[i].update({p[1]:weights[idx]})
                #dict[i].append(p[1])
                #dict[i[1]].append(weights[idx])
            elif (p[1] == i):
                dict[i].update({p[0]:weights[idx]})
                #dict[i[0]].append(p[0])
                #dict[i[1]].append(weights[idx])
    return dict                
    

def Prim():
    return 0
     
if __name__ == '__main__':
    N,M,pairs,weights = formatter()
    d = people(N,M,pairs,weights)
    print(d[1])
    print(d[2])
    print(d[3])
    print(d[4])