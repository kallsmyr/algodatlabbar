from re import M
import sys, time
from collections import deque




def formatter():
    # input = open("C:\\Users\\Carl\\Programmering\\EDAF05-labs-public\\2wordladders\\data\\secret\\1small1.in")
    #input = open("C:\\Users\\Isak\\Documents\\AlgoDat\\EDAF05-labs-public\\2wordladders\\data\\secret\\1small1.in")
    #firstLine = input.readline()
    firstLine = sys.stdin.readline()

    firstIdx = firstLine.find(" ") 
    N = int(firstLine[:firstIdx]) 
    #print("Number of words:" + str(N))
    Q = int(firstLine[firstIdx:])
    #print("Number of queries:" + str(Q))
    dict = {}
    words = []
    pairs = []
    for i in range(0, N):
        #line = input.readline().replace("\n","")
        line = sys.stdin.readline().replace("\n","") 
        words.append(line) #We add all words to this list
        dict.update({line : []})  #And then to this dictionary
    for j in range(0, Q): #Here we look at the pairs of words that make up the queries
        #qline = input.readline().replace("\n","")
        qline = sys.stdin.readline().replace("\n","")
        qidx = qline.find(" ") 
        idx1 = words.index(qline[:qidx]) #Index of the start word in words
        idx2 = words.index(qline[qidx+1:]) #Index of the goal word in words
        pairs.append([idx1,idx2])
    return dict, words, pairs
        
def arccheck(word1, word2):
    lettersfound = 0
    wordlist = [word2[0],word2[1],word2[2],word2[3],word2[4]] #the letters of the goalword
    for i in range (1,5):
        letter = word1[i] #The letter we're looking for
        found = False
        for j in range(0,5):
            if ((wordlist[j] == letter) and (found == False)): #We found it
                found = True
                wordlist[j] = '_' #Remove the letter so we dont double-count it
                break #We stop looking when we found our letter
        if found :
            lettersfound += 1
        else : #If any letter wasnt found, there is no arc
            return False
    if lettersfound == 4: #If we found all letters, there is an arc
        return True
    return False

def graphmaker(dict): #O(n^2)
    for i in dict: #From each word in the dictionary
        for j in dict: #To each word in thedictionary
            if i != j: 
                if arccheck(i,j): #We see if there is an arc
                    dict[i].append(j) #If there is, we add the goalword as a neighbor to the startword
                    

def BFS(dict,startword,goalword):
    if startword == goalword:
        return 0
    visited = dict.copy() #We create a dictionary that sees if we've visited each node
    for i in visited:
        visited[i] = 0 #At the start we havent visited any nodes
    visited[startword] = 1 #Except for the start word
    parent = dict.copy() #we create a dictionary that stores each node's parent
    for i in parent:
        parent[i] = None #No parents have been found yet
    q = deque([]) #This is a list of the nodes we have to work with
    q.append(startword)
    while q: #
        #layer += 1
        m = q.popleft() #The word we're looking at

        for neighbor in dict[m]:
            if visited[neighbor] == 0: #If we havent visited this node yet
                parent[neighbor] = m #We add the parent of this node
                visited[neighbor] = 1 #Now we've visited it
                q.append(neighbor) #And add it to nodes to work with
                # pred = neighbor
            if neighbor == goalword: #We found our word
                foundword = neighbor
                layer = 0 
                while parent[foundword] != None: #We work our way up through the parent directory
                    layer +=1 
                    foundword = parent[foundword] #Look at the parent's parent until we find the start word
                return layer #Return how many parents we've gone through
                    
                
    return "Impossible" #We end up here if we run out of nodes to work with
 
if __name__ == '__main__':
    #start = time.time()
    dict , words, pairs = formatter()
    #print("TIME TO FORMAT: " + str(time.time()-start))
    #start = time.time()
    graphmaker(dict)
    #print("TIME TO MAKE GRAPH: " + str(time.time()-start))
    start = time.time()
    #printlist = []
    for i in pairs:
        res = BFS(dict, words[i[0]], words[i[1]])
        print(res)
        #printlist.append(res)
    print("BFS METHOD: " + str(time.time()-start))
    #for i in printlist:
     #   print(i)
    #print(i in printlist)