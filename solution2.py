from re import M
import sys, time
from collections import deque




def formatter():
    # input = open("C:\\Users\\Carl\\Programmering\\EDAF05-labs-public\\2wordladders\\data\\secret\\1small1.in")
    # firstLine = input.readline()
    firstLine = sys.stdin.readline()

    firstIdx = firstLine.find(" ")
    N = int(firstLine[:firstIdx])
    Q = int(firstLine[firstIdx:])
    dict = {}
    words = []
    pairs = []
    for i in range(0, N):
        # line = input.readline().replace("\n","")
        line = sys.stdin.readline().replace("\n","")
        words.append(line)
        dict.update({line : []}) 
    for j in range(0, Q):
        # qline = input.readline().replace("\n","")
        qline = sys.stdin.readline().replace("\n","")
        qidx = qline.find(" ")
        idx1 = words.index(qline[:qidx])
        idx2 = words.index(qline[qidx+1:])
        pairs.append([idx1,idx2])
    return dict, words, pairs
        
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

def graphmaker(dict): #O(n^2)
    for i in dict:
        for j in dict:
            if i != j:
                if arccheck(i,j):
                    dict[i].append(j)

def BFS_shortestDistance(graph: dict, start, goal):
    if start == goal:
            return 0
    queue = deque([start])
    visited = deque([start])
    dist = {start: 0, goal:-1}
    while queue:
        node = queue.popleft()
        if node == goal:
            if dist[goal] ==-1:
                dist[node]
            else:
                min(dist[goal], dist[node])
        for adjacent in graph[node]:
            if adjacent not in visited:
                visited.append(adjacent)
                queue.append(adjacent)
                dist[adjacent] = dist[node] + 1
    return dist[goal]



def BFS(dict,startword,goalword):
    layer = 0
    if startword == goalword:
        return 0
    visited = deque([])
    q = deque([])
    # dictlist = list(dict)
    # print(dictlist)
    visited.append(startword)
    q.append(startword)
    # pred = startword
    while q: #Visited istället en lista med 0 om inte besökt, 1 om besökt.
        layer += 1
        m = q.popleft()

        for neighbor in dict[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                q.append(neighbor)
                # pred = neighbor
            if neighbor == goalword:
                return layer
    return "Impossible"

if __name__ == '__main__':
    # dict = {"there":[], "where":[], "input":[], "putin":[], "hello":[], "cheer":[], "sheer":[], "cutin":[], "lolem":[]}
    # print(dict)
    #print(arccheck('there', 'where'))
    start = time.time()
    dict , words, pairs = formatter()
    print("TIME TO FORMAT: " + str(time.time()-start))
    start = time.time()
    graphmaker(dict)
    print("TIME TO MAKE GRAPH: " + str(time.time()-start))
    dictlist = list(dict)
    start = time.time()
    printlist = []
    for i in pairs:
        res = BFS(dict, words[i[0]], words[i[1]])
        printlist.append(res)
    print("BFS METHOD: " + str(time.time()-start))
    print(i in printlist)