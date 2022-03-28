import sys, time

def fixInput(inData):
    start = time.time()
    inData_split = inData.split()
    N = int(inData_split.pop(0))
    inData_split = [int(i) for i in inData_split]
    Wind = []
    lenWind = 0
    W = []
    M = []
    for p in range(0,len(inData_split)-1, N+1):
        if lenWind == N: #Unnecessary to search in Wind if it is already filled.
            M.append(inData_split[p:p+N+1])
        else:
            if inData_split[p] not in Wind:
                Wind.append(inData_split[p])
                lenWind= lenWind+1
                W.append(inData_split[p:p+N+1])
            else:
                M.append(inData_split[p:p+N+1])
    W = sorted(W) #Python can sort list of lists by first element with this!
    M = sorted(M)
    end = time.time()
    print("TIME TO FIX INPUT: " + str(end-start)) 
    return N, W, M

def findManList(MenTemp,hisIndex,N): #UNUSED!
    for man in MenTemp:
        if man[0] == hisIndex:
            man = man[1:N+1]
            return man
    return None

def findWomanList(WomenTemp, herIndex,N): #UNUSED!
    for woman in WomenTemp:
        if woman[0] == herIndex:
            woman = woman[1:N+1]
            return woman
    return None

def GS(N,Men, Women):
    start = time.time()
    bachelors = []
    for i in Men:
        bachelors.append(i[0])
    
    mensPartner = [None]*N

    womensPartner = [None]*N

    nextManProposal = [0]*N

    while bachelors:
        him = bachelors[-1]
        hisPreferences = Men[him-1][1:]
        her = hisPreferences[nextManProposal[him-1]]
        herPreferences = Women[her-1][1:]
        currentFiancee = womensPartner[her-1] 

        if currentFiancee == None:
            womensPartner[her-1] = him
            mensPartner[him-1] = her

            nextManProposal[him-1] = nextManProposal[him-1] + 1

            bachelors.pop()
        else:

            idx = herPreferences.index(currentFiancee)



            hisIdx = herPreferences.index(him)
            if hisIdx < idx:
                womensPartner[her-1] = him
                mensPartner[him-1] = her
                nextManProposal[him-1] = nextManProposal[him-1] + 1

                bachelors.pop()
                bachelors.insert(0,currentFiancee)
            else:
                nextManProposal[him-1] = nextManProposal[him-1] + 1

    end = time.time()
    print("GALE-SHAPNEY METHOD'S TIME: " + str(end-start))
    return mensPartner
    
def test(string):
    #string = "2\n1 1 2\n2 2 1\n1 1 2\n2 2 1"
    N, W, M = fixInput(string)
    MenPairs = GS(N,W,M)
    # for i in MenPairs:
    #     print(i)

if __name__ == '__main__':
    start = time.time()
    input = sys.stdin.read()
    # input = open("C:/Users/Carl/Programmering/EDAF05-labs-public/1stablemarriage/data/secret/2testmid.in").read()
    end = time.time()
    print("TIME TO READ FILE FROM stdin-METHOD: " + str(end-start))
    # input = "4\n4 2 1 4 3\n1 3 2 4 1\n1 1 4\n3 2 2 2\n4 3 1 3 1 2 4\n3 3 4 3 1\n2 4\n3 2 4 1 2 1 3 2\n4"
    test(input)
   