import sys
from collections import deque
import time

def formatter():
    input = open("C:\\Users\\Carl\\Programmering\\EDAF05-labs-public\\3makingfriends\\data\\secret\\4huge.in")
    firstline = input.readline()
    space = firstline.find(" ")
    N = int(firstline[:space])
    M = int(firstline[space:])
    print(str(N) + "+" + str(M))
    #pairs = []
    #weights = []
    dict1 = {}
    dict2 = {} #Skapar dictionaries redan här
    for i in range(1,N+1):
        dict1.update({i:[]})
        dict2.update({i:[]})
    for i in range(0,M):
        line = input.readline().replace("\n","")
        space1 = line.find(" ")
        space2 = line.find(" ",space1+1)
        person1 = int(line[:space1])
        person2 = int(line[space1:space2])
        weight = int(line[space2:])
        dict1[person1].append((person2,weight)) #Så kan man lägga in kanter direkt när man får dem
        dict2[person2].append((person1,weight)) #Och behöver inte loopa igen
        #pairs.append([person1,person2])
        #weights.append(weight)
    #for i in dict1:
     #   dict1[i].append(dict2[i])
    #dict1.update(dict2)
    return dict1, dict2

def people(N,pairs,weights): #Dictionary av dictionary (coolt)
    dict = {} #Key är en person, value är en dictionary för alla dess vänner
    # Inre dictionary för varje vän: key är vän value är viken av vänskapen 
    for i in range(1,N+1):
        dict.update({i:[]}) 
        for idx,p in enumerate(pairs):
            if (p[0] == i):
                dict[i].append((p[1],weights[idx]))
                #dict[i].append(p[1])
                #dict[i[1]].append(weights[idx])
            elif (p[1] == i):
                dict[i].append((p[0],weights[idx]))
                #dict[i[0]].append(p[0])
                #dict[i[1]].append(weights[idx])  
    for kvp in dict: #Tänk om
        dict[kvp] = sorted(dict[kvp], key= lambda ele: ele[1])
    return dict               

def dictmerge(dict1,dict2): #Mergar 2 dictionries så vi inte får listor i listor på values
    for i in dict1:
        if dict2[i] == []:
            1
        elif dict1[i] == []:
            dict1[i] = dict2[i]
        else:
            for j in range(0, len(dict2[i])):
                dict1[i].append(dict2[i][j])

    #for k in dict:
     #   s = sorted(dict[i],key=lambda ele:ele[1])
      #  dict1[i] = s 
    return dict1


def Prim(G,r):
    T = []
    totweight = 0
    Q = deque([])
    added = [1]
    for v in r:
        Q.append(v)
    while Q:
        while Q[0][0] in added:
            Q.popleft()
            if len(Q) ==0:
                return totweight
        added.append(Q[0][0])
        T.append(Q[0])
        totweight += Q[0][1]
        if len(T) == len(G):
            return totweight
        

        for tuple in G[Q[0][0]]:
            if tuple[0] not in added:
                Q.append(tuple)
        Q = deque(sorted(Q, key =  lambda ele: ele[1]))

    return totweight       

                
if __name__ == '__main__':
    start = time.time()
    d1, d2 = formatter()
    d = dictmerge(d1,d2)
    print("Time to format:" + str(time.time()-start))