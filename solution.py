import sys,copy, time

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
    end = time.time()
    print("TIME TO READ INPUT: " + str(end-start)) 
    return N, W, M

def findManList(MenTemp,hisIndex):
    for man in MenTemp:
        if man[0] == hisIndex:
            man.pop(0) #remove index
            return man
    return None

def findWomanList(WomenTemp, herIndex):
    for woman in WomenTemp:
        if woman[0] == herIndex:
            woman.pop(0) #remove index
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
        menTemp = copy.deepcopy(Men)
        womenTemp = copy.deepcopy(Women)

        him = bachelors[0]

        hisPreferences = findManList(menTemp, him)

        her = hisPreferences[nextManProposal[him-1]] #STUDERA index -1 är en lösning

        herPreferences = findWomanList(womenTemp, her)

        currentFiancee = womensPartner[her-1] #STUDERA

        if currentFiancee == None:
            womensPartner[her-1] = him
            mensPartner[him-1] = her

            nextManProposal[him-1] = nextManProposal[him-1] + 1

            bachelors.pop(0)
        else:

            idx = herPreferences.index(currentFiancee) #STUDERA DETTA, PÅ SISTA BACHELOR FÅS NONE
            #Nu fås med 1testsmallmessy mensPartners[4 5 2 3], 5an kommer nog ifrån Nextmanproposal + 1!!!




            hisIdx = herPreferences.index(him)
            if hisIdx < idx: #KIKA PÅ OM -1 SKA VARA HÄR! DEBUGGA
                womensPartner[her-1] = him
                mensPartner[him-1] = her
                nextManProposal[him-1] = nextManProposal[him-1] + 1

                bachelors.pop(0)
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
    print(MenPairs)

if __name__ == '__main__':
    i = ""
    for line in sys.stdin:
        i = i + line
    # i = "4\n4 2 1 4 3\n1 3 2 4 1\n1 1 4\n3 2 2 2\n4 3 1 3 1 2 4\n3 3 4 3 1\n2 4\n3 2 4 1 2 1 3 2\n4"
    test(i)
   