# delta = -4 står i problembeskrivning
# Länk till algoritmen https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm
import numpy as np

def formatter():
    input = open("C:\\Users\\kalls\\OneDrive\\Dokument\\EDAF05-labs-public-master\\5gorilla\\data\\secret\\0mini.in")
    #input = open("C:\\Users\\kalls\\OneDrive\\Dokument\\EDAF05-labs-public-master\\5gorilla\\data\\sample\\1.in")
    characters = input.readline().split()
    #print(characters)
    #dict = {}
    alpha = np.zeros((len(characters),len(characters)))
    #alpha = []
    #for i in range(0,len(characters)):
     #   alpha[0][i+1] = characters[i]
      #  alpha[i+1][0] = characters[i]
    for i in range(0,len(characters)):
        line = input.readline().split()
        for j in range(0,len(line)):
            alpha[i][j] = int(line[j])
        
    Q = int(input.readline())
    queries = []
    for i in range(0,Q):
        queries.append(input.readline().split())
    return characters, alpha, queries   


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


def matrixMaker(string1,string2,alpha,delta,characters):
    string1 = list(string1)
    string2 = list(string2)  
    F = np.zeros((len(string1),len(string2))) #numpy är cursed
    for i in range (0,len(string1)):
        F[i,0] = delta*i
    for j in range (0,len(string2)):
        F[0,j] = delta*j
    for i in range (1,len(string1)):
        for j in range (1,len(string2)):
            #opt1 = F[i-1,j-1] + similarity(alpha,string1[i],string2[j],characters)
            #opt2 = F[i-1,j] + delta
            #opt3 = F[i,j-1] + delta
            #F[i,j] = max(opt1,opt2,opt3) 
            F[i,j] = max(F[i-1,j-1] + similarity(alpha,string1[i],string2[j],characters), F[i-1,j] + delta, F[i,j-1] + delta)
    return F

def similarity(matrix,char1,char2,characters):
    pos1 = characters.index(char1)
    pos2 = characters.index(char2)
    return matrix[pos1][pos2]
    
    

def NeedlemanWunsch(string1,string2,F,alpha,delta,characters):
    string1 = list(string1)
    string2 = list(string2)
    i = len(string1)-1
    j = len(string2)-1
    s1 = []
    s2 = []
    while (i >= 0 and j >= 0): #Ibland blir det infinite loop här
        
        if (i>=0 and j>=0 and F[i,j] == F[i-1,j-1] + similarity(alpha,string1[i],string2[j],characters)): #No displacement, we change nothing
            s1.append(string1[i])
            s2.append(string2[j])
            i -=1
            j -=1
        elif (i>=0 and F[i,j] == F[i,j-1] + delta): #Missing character in string1
            #string1.insert(i,'*')
            s1.append('*')
            s2.append(string2[j])
            i -=1
        elif ((F[i,j] == F[i-1,j] + delta)): #or (i==0 and j==0)): #Missing character in string2
            #string2.insert(j,'*')
            s1.append(string1[i])
            s2.append('*')
            j -=1
    #for i in range(0,len(string1)):
    #s = ""    
    s1.append(string1[0]) #Nödlösning för att den loopar en gång för lite
    s2.append(string2[0])
    return "".join(s1)[::-1],"".join(s2)[::-1]
        

    nx = len(x)
    ny = len(y)
    # Optimal score at each possible pair of characters.
    F = np.zeros((nx + 1, ny + 1))
    F[:,0] = np.linspace(0, -nx, nx + 1)
    F[0,:] = np.linspace(0, -ny, ny + 1)
    # Pointers to trace through an optimal aligment.
    P = np.zeros((nx + 1, ny + 1))
    P[:,0] = 3
    P[0,:] = 4
    # Temporary scores.
    t = np.zeros(3)
    for i in range(nx):
        for j in range(ny):
            if x[i] == y[j]:
                t[0] = F[i,j] + match
            else:
                t[0] = F[i,j] - mismatch
            t[1] = F[i,j+1] - gap
            t[2] = F[i+1,j] - gap
            tmax = np.max(t)
            F[i+1,j+1] = tmax
            if t[0] == tmax:
                P[i+1,j+1] += 2
            if t[1] == tmax:
                P[i+1,j+1] += 3
            if t[2] == tmax:
                P[i+1,j+1] += 4
    # Trace through an optimal alignment.
    i = nx
    j = ny
    rx = []
    ry = []
    while i > 0 or j > 0:
        if P[i,j] in [2, 5, 6, 9]:
            rx.append(x[i-1])
            ry.append(y[j-1])
            i -= 1
            j -= 1
        elif P[i,j] in [3, 5, 7, 9]:
            rx.append(x[i-1])
            ry.append('-')
            i -= 1
        elif P[i,j] in [4, 6, 7, 9]:
            rx.append('-')
            ry.append(y[j-1])
            j -= 1
    # Reverse the strings.
    rx = ''.join(rx)[::-1]
    ry = ''.join(ry)[::-1]
    return rx,ry 
        
if __name__ == '__main__':
    characters, alpha, queries = formatter()
    for i in queries:
        F = matrixMaker(i[0],i[1],alpha,-4,characters)
        string1, string2 = NeedlemanWunsch(i[0],i[1],F,alpha,-4,characters)
        #string1, string2 = nw(i[0],i[1])
        print(string1 + " " + string2)