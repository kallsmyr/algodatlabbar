import sys
import time

def input():
    N = int(sys.stdin.readline()) #Read first line which is always the single integer.
    remainder = 2*N*(N+1)
    nbrs = [0]*remainder
    while remainder > 0: #get the numbers in integer form from input
        idx = 2*N*(N+1) - remainder
        line = [int(i) for i in sys.stdin.readline().split()]
        nbrs[idx:idx+len(line)] = line
        remainder -= len(line)
    M = []
    W = []
    Wind = []
    lenWind = 0
    for p in range(0,len(nbrs), N+1):
        if lenWind ==N:
            M.append(nbrs[p:p+N+1])
        else:
            if nbrs[p] not in Wind:
                Wind.append(nbrs[p])
                lenWind +=1
                W.append(nbrs[p:p+N+1])
            else:
                M.append(nbrs[p:p+N+1])
    W = sorted(W, reverse = False)  # Python can sort list of lists by first element with this!
    M = sorted(M, reverse = False)
    return M, W


def MenByIndex(Women): #The GS algorithm produces the stable matching which is worst for women >:(
#We ought to store each woman´s preferences as indexes.
    N = len(Women)
    newW = [None]*N
    temp = [0]*(N*(N+1))
    for i_w in range(0,N):
        temp[i_w*(N+1)] = i_w +1 #women index w_i = i_w +1
        #fixes python indexing 0->N-1
        for m in range(1,N+1):
            pman = Women[i_w][m] #The preferred m:th man for woman i
            temp[i_w*(N+1) + pman] = m
        newW[i_w] = temp[i_w * (N+1) : (i_w + 1)*(N+1)]
    return newW

def GS(M,W):
    bachelors = []  #Bachelors, format is 
    marriedWomen = [None]*len(W) #married women
    W = MenByIndex(W)
    for m in M:
        bachelors.append([m[0],1])
    
    while bachelors:
        him = bachelors.pop()
        her = M[him[0]-1][him[1]]
        him[1] = him[1] + 1
        #  I förra koden sparade vi här i princip currentFiancee = marriedWomen[her-1]
        if marriedWomen[her-1] is None:
            marriedWomen[her-1] = him
        elif W[her-1][him[0]] < W[her-1][marriedWomen[her-1][0]]:
            bachelors.append(marriedWomen[her-1])
            marriedWomen[her-1] = him
        else:
            bachelors.append(him)
    for i in range(0,len(marriedWomen)):
        print(marriedWomen[i][0])

def test():
    M, W = input()
    GS(M,W)

if __name__ == '__main__':
    test()
