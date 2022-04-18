import math
import sys, time

def formatter():
    # input = open("C:\\Users\\Carl\\Programmering\\EDAF05-labs-public\\4closestpair\\data\\secret\\1small.in")
    points = []
    # N = int(input.readline().replace("\n",""))
    N = int(sys.stdin.readline().replace("\n",""))
    for _ in range(N):
        line = sys.stdin.readline().replace("\n", "")
        # line = input.readline().replace("\n", "")
        space = line.find(" ")
        points.append(  ( int(line[:space]), int(line[space:]) ) ) 
    Px = sorted(points, key = lambda point: point[0]) #O(nlogn)
    Py = sorted(points, key = lambda point: point[1]) #O(nlogn)
    return Px, Py

def metric(p1: tuple, p2: tuple, key = "Euclidian"): #Just for fun I added different distance functions.
    if key == "Euclidian":
        return math.sqrt(((p2[0] - p1[0])**2)+((p2[1] - p1[1])**2))
    elif key == "Taxicab":
        return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
    elif key == "Discrete": #Always 1 since input does not contain two points on same coordinates.
        return 0 if p1 == p2 else 1
    else:
        return math.sqrt(((p2[0] - p1[0])**2)+((p2[1] - p1[1])**2))
        
def brute_force(points):
    minDist = 10**10 #upper boundary is 10*9
    p1 = None
    p2 = None
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = metric(points[i], points[j], key = "Euclidian")
            if dist < minDist:
                minDist = dist
                p1, p2 = points[i] , points[j]
    return p1, p2, minDist

def closestPairs(Px, Py):
    N = len(Px)
    if N <= 16: # Brute forcing less means more time spent on recursive splitting and vice versa. 
        # Experimental tests on the 3rd buggest files as N in [2^2,2^6] yielded best stable and fastest at N = 16
        return brute_force(Px)
    else:
        mid = N // 2
        midpoint = Px[mid]
        Lx, Rx = Px[:mid], Px[mid:]
        Ly, Ry = [], []
        for point in Py:
          Ry.append(point) if point[0] > midpoint[0] else Ly.append(point)
        Rp1, Rp2, Rdelta = closestPairs(Rx, Ry)
        Lp1, Lp2, Ldelta = closestPairs(Lx, Ly)
        mp1, mp2, delta = (Lp1, Lp2, Ldelta) if Ldelta < Rdelta else (Rp1, Rp2, Rdelta)
        S = [point for point in Py if midpoint[0] - delta < point[0] < midpoint[0] + delta]
        for i in range(len(S)):
            for j in range(i+1, min(i+7, len(S))): #we only traverse the next 6 squares according to theory
                dist = metric(S[i], S[j])
                if dist < delta:
                    mp1, mp2, delta = S[i], S[j], dist
    return mp1, mp2, delta


if __name__ == '__main__':
    Px, Py = formatter()
    # start = time.time()
    _, _, minDist = closestPairs(Px,Py) # minx, miny, minDist = also..
    print("{:.6f}".format(minDist))
    # print("ALGORITHM'S TIME: " + str(time.time() - start))
    # print("Points: " + str(minx)+ "---" + str(miny))