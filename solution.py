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

def customInput(filePath):
    start = time.time()
    input = open(filePath)
    N = int(input.readline())
    remainder = 2*N*(N+1)
    nbrs = [0]*remainder
    while remainder > 0: #get the numbers in integer form from input
        idx = 2*N*(N+1) - remainder
        line = [int(i) for i in input.readline().split()]
        nbrs[idx:idx+len(line)] = line
        remainder -= len(line)
    print("TIME TO READ FILE AND CONVERT TO ARRAY OF INTEGER ARRAYS: " + str(time.time()-start))
    start = time.time()
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
    print("TIME TO SORT INTO MEN AND WOMEN ARRAYS: " + str(time.time() - start))
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

def GS(M,W, printOption):
    if printOption == False:
        start = time.time()
    bachelors = []  #Bachelors, format is [bachelor i, #next to propose to]
    marriedWomen = [None]*len(W) #married women
    W = MenByIndex(W) #As the hint suggest we need to reverse the list from value v at index i to index i at value v.
    #  Example: woman i has preflist: 4 1 2 3 -> 2 3 4 1 are the indexes, in python: 1 2 3 0
    for m in M:
        bachelors.append([m[0],1])
    
    while bachelors:
        him = bachelors.pop()
        her = M[him[0]-1][him[1]] #Get his first preferred woman
        him[1] = him[1] + 1 #If this man looses his marriage to his fist preferred woman, then he'd like to marry the next woman in his prefList
        #  I förra koden sparade vi här i princip currentFiancee = marriedWomen[her-1], 
        # men verkade som att currentFiancee inte hade samma minnesadress som marriedWomen[her-1]. Går lika bra att undvika en tempvariabel i detta fall.
        if marriedWomen[her-1] is None:
            marriedWomen[her-1] = him
        elif W[her-1][him[0]] < W[her-1][marriedWomen[her-1][0]]:
            bachelors.append(marriedWomen[her-1])
            marriedWomen[her-1] = him
        else:
            bachelors.append(him)
    if printOption == True:
        for i in range(0,len(marriedWomen)):
         print(marriedWomen[i][0])
    else:
        print("TIME TO PERFORM GALE-SHAPNEY METHOD: " + str(time.time() - start))

def test():
    M, W = input()
    GS(M,W, True)

def testTimeComplexity(SearchPath): #either sample/1.in or sample/2.in OR secret/#testxxxx.in
    dir = "C:\\Users\\Carl\\Programmering\\EDAF05-labs-public\\1stablemarriage\\data\\"
    filePath = str(dir + SearchPath)
    print("TIME COMPLEXITY FOR " + SearchPath)
    start = time.time()
    M, W = customInput(filePath)
    GS(M,W,False)
    print("TOTAL RUNTIME: " + str(time.time() - start))

def testAllTC():
    start = time.time()
    testTimeComplexity("sample\\1.in")
    print("\n")
    testTimeComplexity("sample\\2.in")
    print("\n")
    testTimeComplexity("secret\\0testsmall.in")
    print("\n")
    testTimeComplexity("secret\\1testsmallmessy.in")
    print("\n")
    testTimeComplexity("secret\\2testmid.in")
    print("\n")
    testTimeComplexity("secret\\3testlarge.in")
    print("\n")
    testTimeComplexity("secret\\4testhuge.in")
    print("\n")
    testTimeComplexity("secret\\5testhugemessy.in")
    print("\n")
    print("----------------------------------------------")
    print("RUNTIME FOR ALL TESTS: " + str(time.time() - start))

if __name__ == '__main__':
    test()
    # testTimeComplexity("secret\\5testhugemessy.in") # "secret\\4testhuge.in" , "secret\\0testsmall.in" , "secret\\1testsmallmessy.in", "secret\\2testmid.in" , "secret\\3testlarge.in" , "secret\\5testhugemessy.in", "sample\\1.in" , "sample\\2.in"
    # testAllTC()