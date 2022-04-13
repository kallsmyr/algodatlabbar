import sys
from heapq import heappush, heappop
import time
from random import randint

def formatter():
    # input = open("C:\\Users\\Carl\\Programmering\\EDAF05-labs-public\\3makingfriends\\data\\secret\\1small.in")
    firstline = sys.stdin.readline()
    # firstline = input.readline()

    space = firstline.find(" ")
    N = int(firstline[:space])
    M = int(firstline[space:])
    # print(str(N) + "+" + str(M))
    #pairs = []
    #weights = []
    dict1 = {}
    dict2 = {} #Skapar dictionaries redan här
    for i in range(1,N+1):
        dict1.update({i:[]})
        dict2.update({i:[]})
    for i in range(0,M):
        # line = input.readline().replace("\n","")
        line = sys.stdin.readline().replace("\n","")
        space1 = line.find(" ")
        space2 = line.find(" ",space1+1)
        person1 = int(line[:space1])
        person2 = int(line[space1:space2])
        weight = int(line[space2:])
        dict1[person1].append((person2,weight)) #Så kan man lägga in kanter direkt när man får dem
        dict2[person2].append((person1,weight)) #Och behöver inte loopa igen
    for i in dict1:
        if dict2[i] == []:
            continue
        elif dict1[i] == []:
            dict1[i] = dict2[i]
        else:
            for j in range(0, len(dict2[i])):
                dict1[i].append(dict2[i][j])
    return dict1

def MST_Jarnik(G):
    totw = 0
    added = set() #
    r = randint(1,len(G)) #Pick a random node as root node to ascertain no bias is present.
    Q = [(0,r)] #No cost for starting at the root node r, 
    # heappop() evaluates the first index value then the second if tie, so we just reverse the tuple order in Q
    while Q: #Time complexity: O(n log(n)) 
        weight, friend = heappop(Q)
        if friend not in added:
            added.add(friend)
            totw += weight
            if len(G) == len(added): #Without this, 4huge.in takes 19 seconds, with this it only takes 7.5 seconds
                return totw
            for stranger, weight in G[friend]:
                if stranger not in added:
                    heappush(Q, (weight, stranger)) #stranger becomes friend
    return totw
                
if __name__ == '__main__':
    print(MST_Jarnik(formatter()))