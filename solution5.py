# delta = -4 står i problembeskrivning
# Länk till algoritmen https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm
import numpy as np
import sys

def formatter():
    # input = open("C:\\Users\\Carl\\Programmering\\EDAF05-labs-public\\5gorilla\\data\\sample\\1.in")
    # characters = sys.stdin.readline().split()
    # characters = input.readline().split()
    chars = {char: idx for idx, char in enumerate(sys.stdin.readline().split())}
    # chars = {char: idx for idx, char in enumerate(input.readline().split())}

    alpha = np.zeros((len(chars),len(chars)))

    for i in range(0,len(chars)):
        # line = input.readline().split()
        line = sys.stdin.readline().split()
        for j in range(0,len(line)):
            alpha[i][j] = int(line[j])
        
    # Q = int(input.readline())
    Q = int(sys.stdin.readline())
    queries = []

    for i in range(0,Q):
        # queries.append(input.readline().split())
        queries.append(sys.stdin.readline().split())

    return chars, alpha, queries   

def matrixMaker(string1,string2,alpha,delta,characters):
    string1 = {idx: char for idx, char in enumerate(string1)} #kan göra dictionary fast ha idx:char istället...
    string2 = {idx: char for idx, char in enumerate(string2)}  
    # print(string1)  

    F = np.zeros((len(string1)+1,len(string2)+1)) 
    for i in range (0,np.shape(F)[0]):
        F[i,0] = delta*i
    for j in range (0,np.shape(F)[1]):
        F[0,j] = delta*j
    for i in range (1,np.shape(F)[0]):
        for j in range (1,np.shape(F)[1]):
            MATCH = F[i-1,j-1] + similarity(alpha,string1[i-1],string2[j-1],characters)
            INSERT = F[i-1,j] + delta
            DELETE = F[i,j-1] + delta
            F[i,j] = max(MATCH, DELETE, INSERT) 
            # F[i,j] = max(F[i-1,j-1] + similarity(alpha,string1[i],string2[j],characters), F[i,j-1] + delta,  F[i-1,j] + delta)
    return F

def similarity(matrix,char1,char2,characters):
    return matrix[characters[char1]][characters[char2]]

def NeedlemanWunsch(string1,string2,F,alpha,delta,characters):
    string1 = {idx: char for idx, char in enumerate(string1)} #kan göra dictionary fast ha idx:char istället... :3
    string2 = {idx: char for idx, char in enumerate(string2)}
    i = len(string1)
    j = len(string2)
    s1 = []
    s2 = []
    
    while (i > 0 or j > 0):
        
        if (i>0 and j>0 and F[i,j] == F[i-1,j-1] + similarity(alpha,string1[i-1],string2[j-1],characters)): #No displacement, we change nothing
            s1.append(string1[i-1])
            s2.append(string2[j-1])
            i -=1
            j -=1
        elif (i>=0 and F[i,j] == F[i-1,j] + delta): #Missing character in string1
            s1.append(string1[i-1])
            s2.append("*")
            i -=1
        else:
            s1.append("*")
            s2.append(string2[j-1])
            j -=1

    return "".join(s1)[::-1], "".join(s2)[::-1] #join takes O(1) so that's good!

        
if __name__ == '__main__':
    characters, alpha, queries = formatter()
    for i in queries:
        F = matrixMaker(i[0],i[1],alpha,-4,characters)
        string1, string2 = NeedlemanWunsch(i[0],i[1],F,alpha,-4,characters)
        print(string1 + " " + string2) #check solution takes 2 min: 47.36 sec
