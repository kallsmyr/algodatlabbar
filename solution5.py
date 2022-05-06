# delta = -4 står i problembeskrivning
# Länk till algoritmen https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm
import numpy as np

def formatter():
    input = open("C:\\Users\\kalls\\OneDrive\\Dokument\\EDAF05-labs-public-master\\5gorilla\\data\\sample\\1.in")
    #input = open("C:\\Users\\kalls\\OneDrive\\Dokument\\EDAF05-labs-public-master\\5gorilla\\data\\sample\\1.in")
    characters = input.readline().split()
    #print(characters)
    #dict = {}
    alpha = np.empty(shape=(len(characters),len(characters)))
    #alpha = []
    for i in range(0,len(characters)):
        line = input.readline().split()
        for j in range(0,len(line)):
            alpha[i][j] = int(line[j])
        
    Q = int(input.readline())
    queries = []
    for i in range(0,Q):
        queries.append(input.readline().split())
    return characters, alpha, queries   #Vad ska jag ha alpha till?


def CompareStrings(characters,alpha,string1,string2):    
    string1 = list(string1)
    string2 = list(string2)
    i = 0
    while i < len(string1) or i < len(string2):
        if string1[i] != string2[i]:
            if (len(string2) > i+1):
                if (string1[i] == string2[i+1]): #Missing character in string2
                    string1.insert(i,'*')
            if (len(string1) > i):
                if (string2[i] == string1[i+1]): #Missing character in string1
                    string2.insert(i,'*')
        #Vad gör jag med hopblandade tecken? inget?
        i +=1
                #if (string1(i+1) == string2(i+1)):
    s = ""
    return s.join(string1), s.join(string2)


def matrixMaker(string1,string2,alpha,delta):
    string1 = list(string1)
    string2 = list(string2)  
    F = np.empty(shape=(len(string2)+1,len(string1)+1)) #numpy är cursed
    for i in range (0,len(string1)):
        F[i,0] = delta*i
    for j in range (0,len(string2)):
        F[0,j] = delta*j
    for i in range (1,len(string1)):
        for j in range (1,len(string2)):
            F[i,j] = max(F[i-1,j-1] + alpha[i,j], F[i-1,j] + delta, F[i,j-1] + delta)
    return F

def NeedlemanWunsch(string1,string2,F,alpha,delta):
    string1 = list(string1)
    string2 = list(string2)
    i = len(string1)
    j = len(string2)
    while (i > 0 and j > 0):
        if (F[i,j] == F[i-1,j-1] + alpha[i,j]): #Match, we change nothing
            i -=1
            j -=1
        elif (F[i,j] == F[i-1,j] + delta): #Missing character in string1
            string1.insert('*',i)
            i -=1
        elif (F[i,j] == F[i,j-1] + delta): #Missing character in string2
            string2.insert('*',j)
            j -=1
    return string1,string2
        
        
        
if __name__ == '__main__':
    characters, alpha, queries = formatter()
    for i in queries:
        F = matrixMaker(i[0],i[1],alpha,-4)
        string1, string2 = NeedlemanWunsch(i[0],i[1],F,alpha,-4)
        print(string1 + " " + string2)