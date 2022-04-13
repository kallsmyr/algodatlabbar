import math
import sys, time
from heapq import heappush, heappop
def formatter():
    input = open("C:\\Users\\Carl\\Programmering\\EDAF05-labs-public\\4closestpair\\data\\secret\\1small.in")
    Px = []
    Py = []
    N = int(input.readline().replace("\n",""))
    # N = int(sys.stdin.readline().split().replace("\n",""))
    # firstNLine = input.readline().replace("\n", "")
    # # firstNLine = sys.stdin.readline().replace("\n", "")
    # firstSpace = 
    for i in range(N):
        # line = sys.stdin.readline().replace("\n", "")
        line = input.readline().replace("\n", "")
        space = line.find(" ")
        Px.append(int(line[:space])) 
        Py.append(int(line[space:]))
    mergeSort(Px)
    mergeSort(Py)
    return N, Px, Py

def mergeSort(ints): #mergeSort för Px och Py, kanske kan man skicka med lambdauttryck för att kolla koordinater...
    if len(ints) > 1:
        mid = len(ints) // 2
        L = ints[:mid]
        R = ints[mid:]
        mergeSort(L)
        mergeSort(L) 
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                ints[k] = L[i]
                i += 1
            else:
                ints[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            ints[k] = R[i]
            i += 1
            k += 1
        while j < len(R):
            ints[k] = R[j]
            j += 1
            k += 1



def closestPairs(Px, Py, N): #ToDo....
    mid = N // 2
    Lx = Px[:mid]
    Rx = Px[mid:]
    Ly = Py[:mid]
    Ry = Py[mid:]

        

if __name__ == '__main__':
    N, Px, Py = formatter()
    closestPairs(Px,Py,N)