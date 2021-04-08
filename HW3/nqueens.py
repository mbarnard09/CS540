import random



def succ(state, static_x, static_y):
    emptyList = []
    localList = state[:]
    plus = 0
    minus = 0
    lists = []

    #checking if list has no queen at static point
    if localList[static_x] != static_y:
        return emptyList

    for x in range(0, len(localList)):
        workingListMinus = localList[:]
        workingListPlus = localList[:]
        if x != static_x:
            plus = localList[x] + 1
            minus = localList[x] - 1
            if plus < len(localList):
                workingListPlus[x] = plus
                lists.append(workingListPlus)
            if minus >= 0:
                workingListMinus[x] = minus
                lists.append(workingListMinus)


    #print(sorted(lists))
    return(sorted(lists))

def f(state):
    localList = state[:]
    #queens being attacked
    count = 0

    #x represents each piece being tested
    for x in range(0, len(localList)):
        #comparing x to the other pieces
        for y in range(0, len(localList)):
            #dont compare a piece to itself
            if x == y:
                #print('continued', x, ':', y)
                continue

            #this tests if row attack is available
            if localList[x] == localList[y]:
                count = count + 1
                #print('breakrow', x, ':', y)
                break
            #this tests if diagnal attack is available
            if abs(x-y) == abs(localList[x] - localList[y]):
                count = count + 1
                #print('breakdiag', x, ':', y)
                break
    return count

def choose_next(curr, static_x, static_y):
    fScoreIndexList = []
    lowestList = []
    succStates = succ(curr, static_x,static_y)
    #if state is invalid
    if not succStates:
        #print('NONE')
        return None

    #apparently adding current state to succ states
    succStates.append(curr)
    succStates = sorted(succStates)


    lowestState = succStates[0]
    fScores = []



    for x in succStates:
        fScores.append(f(x))

    #print(succStates)
    #print(fScores)

    #finding the lowest fScore
    minF = min(fScores)
    #finding number of times lowest score occurs
    counter = fScores.count(minF)

    #if the lowest f score is unique
    if counter == 1:
        index = fScores.index(minF)
        #print(succStates[index])
        return succStates[index]

    #if the lowest f score is not unique
    elif counter > 1:
        #this for loop takes the numbers in fscore and checks what index's of
        #the succstates list contain the minF score
        for x in range(0, len(fScores)):
            if fScores[x] == minF:
                fScoreIndexList.append(x)
        for x in fScoreIndexList:
            lowestList.append(succStates[x])

        lowestList = sorted(lowestList)
        #print(lowestList[0])
        return lowestList[0]

def n_queenshelp(initial_state, static_x, static_y):
     localList = initial_state
     workingList = localList[:]
     while True:
        firstFValue = f(workingList)
        #print(workingList, "- f={}".format(f(workingList)))

        if f(workingList) == 0:
            return workingList
            break

        workingList = choose_next(workingList, static_x, static_y)

        secondFValue = f(workingList)

        if firstFValue == secondFValue:
            #print(workingList, "- f={}".format(f(workingList)))
            return workingList
            break

def n_queens(initial_state, static_x, static_y):
     localList = initial_state
     workingList = localList[:]
     while True:
        firstFValue = f(workingList)
        print(workingList, "- f={}".format(f(workingList)))

        if f(workingList) == 0:
            return workingList
            break

        workingList = choose_next(workingList, static_x, static_y)

        secondFValue = f(workingList)

        if firstFValue == secondFValue:
            print(workingList, "- f={}".format(f(workingList)))
            return workingList
            break

def n_queens_restart(n, k, static_x, static_y):
    random.seed(1)
    bestList = []
    reached = 0
    result = []
    bestDict = {}
    finalList = []

    #will run k times
    for i in range(0,k):
        #getting inital state
        Dict = {}
        initialState = []
        for x in range(0, n):
            if x == static_x:
                Dict[x] = static_y
                initialState.append(Dict[x])
            else:
                Dict[x] = random.randint(0,n-1)
                initialState.append(Dict[x])

        if f(n_queenshelp(initialState, static_x, static_y)) == 0:
            result = (n_queenshelp(initialState, static_x, static_y))
            reached = 1
            break

        else:
            bestList.append(n_queenshelp(initialState, static_x, static_y))
            bestDict[i] = f(n_queenshelp(initialState, static_x, static_y))
            continue

    if reached == 1:
        print(result)
    else:
        #print(bestList)
        #print((bestDict))
        minValue = min(bestDict.values())
        for key,value in bestDict.items():
            if value == minValue:
                finalList.append(bestList[key])

        finalList = sorted(finalList)
        for x in finalList:
            print(x)
