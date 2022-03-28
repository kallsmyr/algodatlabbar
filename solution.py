import sys
import time


def fixInput(inData):
    # start = time.time()
    inData_split = inData.split()
    N = int(inData_split.pop(0))
    inData_split = [int(i) for i in inData_split]
    Wind = []
    lenWind = 0
    W = []
    M = []
    for p in range(0, len(inData_split)-1, N+1):
        if lenWind == N:  # Unnecessary to search in Wind if it is already filled.
            M.append(inData_split[p:p+N+1])
        else:
            if inData_split[p] not in Wind:
                Wind.append(inData_split[p])
                lenWind = lenWind+1
                W.append(inData_split[p:p+N+1])
            else:
                M.append(inData_split[p:p+N+1])
    W = sorted(W)  # Python can sort list of lists by first element with this!
    M = sorted(M)
    # print("TIME TO FIX INPUT: " + str(time.time() - start))
    return N, W, M


def GS(N, Men, Women):
    # start = time.time()
    bachelors = []
    for i in Men:
        bachelors.append(i[0])
    mensPartner = [None]*N
    womensPartner = [None]*N
    nextManProposal = [0]*N
    while bachelors:
        him = bachelors[-1]
        hisPref = Men[him-1][1:]
        her = hisPref[nextManProposal[him-1]]
        herPref = Women[her-1][1:]
        currentFiancee = womensPartner[her-1]
        if currentFiancee == None:
            womensPartner[her-1] = him
            mensPartner[him-1] = her
            nextManProposal[him-1] = nextManProposal[him-1] + 1
            bachelors.pop()
        else:

            idx = herPref.index(currentFiancee)
            hisIdx = herPref.index(him)
            if hisIdx < idx:
                womensPartner[her-1] = him
                mensPartner[him-1] = her
                nextManProposal[him-1] = nextManProposal[him-1] + 1
                bachelors.pop()
                bachelors.insert(-1, currentFiancee)
            else:
                nextManProposal[him-1] = nextManProposal[him-1] + 1
    # print("GALE-SHAPNEY METHOD'S TIME: " + str(time.time() -  start))
    return mensPartner


def test(string):
    #string = "2\n1 1 2\n2 2 1\n1 1 2\n2 2 1"
    N, W, M = fixInput(string)
    MenPairs = GS(N, W, M)
    # for i in MenPairs:
    #     print(i)
    for i in range(0,len(MenPairs)-1):
        print(MenPairs[i])
    print(MenPairs[len(MenPairs)-1], end = "")

if __name__ == '__main__':
    # start = time.time()
    input = sys.stdin.read()
    # input = open("C:/Users/Carl/Programmering/EDAF05-labs-public/1stablemarriage/data/sample/2.in").read()
    # print("TIME TO READ FILE FROM stdin-METHOD: " + str(time.time() - # start))
    # input = "4\n4 2 1 4 3\n1 3 2 4 1\n1 1 4\n3 2 2 2\n4 3 1 3 1 2 4\n3 3 4 3 1\n2 4\n3 2 4 1 2 1 3 2\n4"
    test(input)
