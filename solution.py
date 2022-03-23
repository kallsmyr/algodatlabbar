import numpy as np

def split_list(a_list):
        half = len(a_list)//2
        return a_list[:half], a_list[half:]

def format(inData):
    #nbrofPairs = int(inData[:inData.find("\n",0,4)]) #Hitta N \in (1,3000) genom att hitta första radbrytningen som kan finnas i index [0,3].
    inData_split = inData.split()
    nbrofpairs = int(inData_split.pop(0))
    inData_split = [int(i)-1 for i in inData_split]
    idx_list = []

    for i in range(0, len(inData_split),1):
        if i%(nbrofpairs+1) == 0:
            idx_list.append(i)
    res = [ele for idx, ele in enumerate(inData_split) if idx not in idx_list] 

    W,M = split_list(res) 
    WLinked = []
    MLinked = []
    for i in range(0,len(W), 2) :
        WLinked.append(W[i:i+nbrofpairs])
        MLinked.append(M[i:i+nbrofpairs])
    print("MLinked: ")
    print(MLinked)
    print("WLinked: ")
    print(WLinked)
    # r_shape = int(len(W)**0.5)
    # W = np.array([W]).reshape(r_shape, r_shape + nbrofpairs)
    # M = np.array([M]).reshape(r_shape, r_shape + nbrofpairs)
   
    return [nbrofpairs,WLinked,MLinked] #return the list of men and women

def GS(N,Men, Women):

    bachelors = list(range(N))

    mensPartner = [None]*N

    womensPartner = [None]*N

    nextManProposal = [0]*N

    while bachelors:

        him = bachelors[0]

        hisPreferences = Men[him]

        her = hisPreferences[nextManProposal[him]]

        herPreferences = Women[her]

        currentFiancee = womensPartner[her]

        if currentFiancee == None:
            womensPartner[her] = him
            mensPartner[him] = her

            nextManProposal[him] = nextManProposal[him] + 1

            bachelors.pop(0)
        else:

            idx = herPreferences.index(currentFiancee)
            hisIdx = herPreferences.index(him)
            if hisIdx < idx:
                womensPartner[her] = him
                mensPartner[him] = her
                nextManProposal[him] = nextManProposal[him] + 1

                bachelors.pop(0)
                bachelors.insert(0,currentFiancee)
            else:
                nextManProposal[him] = nextManProposal[him] + 1
    mensPartner = [i +1 for i in mensPartner]
    return mensPartner

    #Gale-Shapney Algorithm
    #p = [m+1 for m in range(len(M))]
    # while p != None:
    #     m = p[i]
    #     w = p[i][0]
    #     i = i +1
    



def test():
    string = "2\n1 1 2\n2 2 1\n1 1 2\n2 2 1"
    N, W,M = format(string)
    MenPairs = GS(N=N, Women = W, Men = M)
    print(MenPairs)
if __name__ == '__main__':
    test()