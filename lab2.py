# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 10:30:02 2022

@author: Isak
"""

def arccheck(word1, word2):
    lettersfound = 0
    #letters = [start[1], start[2], start[3], start[4]]
    wordlist = []
    for k in range(0,5):
        wordlist.append(word2[k])
    for i in range (1,5):
        letter = word1[i]
        found = False
        for j in range(0,5):
            if ((wordlist[j] == letter) and (found == False)):
                found = True
                wordlist[j] = '_'
        if found :
            lettersfound += 1
    if lettersfound == 4:
        return True
    return False

def graphmaker(dict):#O(n^2)
    for i in dict:
        for j in dict:
            if i != j:
                if arccheck(i,j):
                    dict[i].append(j)

def BFS(dict,startword,goalword,N):
    layer = 0
    visited = [0]*N
    dictlist = list(dict)
    #print(dictlist)
    words = [startword]
    while (len(words) > 0):
        layer += 1
        neighbors = dict[words.pop()]
        for i in neighbors:
            idx = dictlist.index(i)
            if visited[idx] == 0:
                if i == goalword:
                    return layer
                visited[idx] = 1
                words.append(i)
    return "Impossible"
        
            
    



if __name__ == '__main__':
    dict = {"there":[], "where":[], "input":[], "putin":[], "hello":[], "cheer":[], "sheer":[], "cutin":[], "lolem":[]}
    graphmaker(dict)
    print(dict)
    print(BFS(dict,"input","cutin",len(dict)))
    #print(arccheck('there', 'where'))
    