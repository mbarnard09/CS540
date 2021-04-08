import numpy as np
import heapq

#for printing succesors
def print_succ(list):
    localList = list[:]
    localList2 = list[:]
    localList3 = list[:]
    localList4 = list[:]
    lists = []
    for x in localList:
        if x == 0:
            index = list.index(x)
            break
    if index == 0:
        localList[0] = list[1]
        localList[1] = list[0]

        localList2[0] = list[3]
        localList2[3] = list[0]

        lists.append(localList)
        lists.append(localList2)

        lists = sorted(lists)
        for j in range(0,len(lists)):
            print(lists[j],'h={}'.format(manhattan(lists[j])))

    elif index == 1:
        localList[0] = list[1]
        localList[1] = list[0]

        localList2[1]=list[2]
        localList2[2] = list[1]

        localList3[1] =list[4]
        localList3[4]= list[1]

        lists.append(localList)
        lists.append(localList2)
        lists.append(localList3)

        lists = sorted(lists)
        for j in range(0,len(lists)):
            print(lists[j],'h={}'.format(manhattan(lists[j])))

    elif index == 2:
        localList[1] = list[2]
        localList[2] = list[1]

        localList2[2] = list[5]
        localList2[5] = list[2]

        lists.append(localList)
        lists.append(localList2)

        lists = sorted(lists)
        for j in range(0,len(lists)):
            print(lists[j],'h={}'.format(manhattan(lists[j])))

    elif index == 3:
        localList[3] = list[0]
        localList[0] = list[3]

        localList2[4]=list[3]
        localList2[3] = list[4]

        localList3[6] =list[3]
        localList3[3]= list[6]

        lists.append(localList)
        lists.append(localList2)
        lists.append(localList3)

        lists = sorted(lists)
        for j in range(0,len(lists)):
            print(lists[j],'h={}'.format(manhattan(lists[j])))

    elif index == 4:
        localList[4] = list[1]
        localList[1] = list[4]

        localList2[3]=list[4]
        localList2[4] = list[3]

        localList3[5] =list[4]
        localList3[4]= list[5]

        localList4[7] =list[4]
        localList4[4]= list[7]

        lists.append(localList)
        lists.append(localList2)
        lists.append(localList3)
        lists.append(localList4)

        lists = sorted(lists)
        for j in range(0,len(lists)):
            print(lists[j],'h={}'.format(manhattan(lists[j])))

    elif index == 5:
        localList[2] = list[5]
        localList[5] = list[2]

        localList2[4]=list[5]
        localList2[5] = list[4]

        localList3[8] =list[5]
        localList3[5]= list[8]

        lists.append(localList)
        lists.append(localList2)
        lists.append(localList3)

        lists = sorted(lists)
        for j in range(0,len(lists)):
            print(lists[j],'h={}'.format(manhattan(lists[j])))

    elif index == 6:
        localList[7] = list[6]
        localList[6] = list[7]

        localList2[3] = list[6]
        localList2[6] = list[3]

        lists.append(localList)
        lists.append(localList2)

        lists = sorted(lists)
        for j in range(0,len(lists)):
            print(lists[j],'h={}'.format(manhattan(lists[j])))

    elif index == 7:
        localList[4] = list[7]
        localList[7] = list[4]

        localList2[6]=list[7]
        localList2[7] = list[6]

        localList3[8] =list[7]
        localList3[7]= list[8]

        lists.append(localList)
        lists.append(localList2)
        lists.append(localList3)

        lists = sorted(lists)
        for j in range(0,len(lists)):
            print(lists[j],'h={}'.format(manhattan(lists[j])))

    elif index == 8:
        localList[5] = list[8]
        localList[8] = list[5]

        localList2[7] = list[8]
        localList2[8] = list[7]

        lists.append(localList)
        lists.append(localList2)

        lists = sorted(lists)
        for j in range(0,len(lists)):
            print(lists[j],'h={}'.format(manhattan(lists[j])))

def succ(list):
    localList = list[:]
    localList2 = list[:]
    localList3 = list[:]
    localList4 = list[:]
    lists = []
    index = 0
    for x in localList:
        if x == 0:
            index = list.index(x)
            break
    if index == 0:
        localList[0] = list[1]
        localList[1] = list[0]

        localList2[0] = list[3]
        localList2[3] = list[0]

        lists.append(localList)
        lists.append(localList2)

        lists = sorted(lists)
        return lists

    elif index == 1:
        localList[0] = list[1]
        localList[1] = list[0]

        localList2[1]=list[2]
        localList2[2] = list[1]

        localList3[1] =list[4]
        localList3[4]= list[1]

        lists.append(localList)
        lists.append(localList2)
        lists.append(localList3)

        lists = sorted(lists)
        return lists

    elif index == 2:
        localList[1] = list[2]
        localList[2] = list[1]

        localList2[2] = list[5]
        localList2[5] = list[2]

        lists.append(localList)
        lists.append(localList2)

        lists = sorted(lists)
        return lists

    elif index == 3:
        localList[3] = list[0]
        localList[0] = list[3]

        localList2[4]=list[3]
        localList2[3] = list[4]

        localList3[6] =list[3]
        localList3[3]= list[6]

        lists.append(localList)
        lists.append(localList2)
        lists.append(localList3)

        lists = sorted(lists)
        return lists

    elif index == 4:
        localList[4] = list[1]
        localList[1] = list[4]

        localList2[3]=list[4]
        localList2[4] = list[3]

        localList3[5] =list[4]
        localList3[4]= list[5]

        localList4[7] =list[4]
        localList4[4]= list[7]

        lists.append(localList)
        lists.append(localList2)
        lists.append(localList3)
        lists.append(localList4)

        lists = sorted(lists)
        return lists

    elif index == 5:
        localList[2] = list[5]
        localList[5] = list[2]

        localList2[4]=list[5]
        localList2[5] = list[4]

        localList3[8] =list[5]
        localList3[5]= list[8]

        lists.append(localList)
        lists.append(localList2)
        lists.append(localList3)

        lists = sorted(lists)
        return lists

    elif index == 6:
        localList[7] = list[6]
        localList[6] = list[7]

        localList2[3] = list[6]
        localList2[6] = list[3]

        lists.append(localList)
        lists.append(localList2)

        lists = sorted(lists)
        return lists

    elif index == 7:
        localList[4] = list[7]
        localList[7] = list[4]

        localList2[6]=list[7]
        localList2[7] = list[6]

        localList3[8] =list[7]
        localList3[7]= list[8]

        lists.append(localList)
        lists.append(localList2)
        lists.append(localList3)

        lists = sorted(lists)
        return lists

    elif index == 8:
        localList[5] = list[8]
        localList[8] = list[5]

        localList2[7] = list[8]
        localList2[8] = list[7]

        lists.append(localList)
        lists.append(localList2)

        lists = sorted(lists)
        return lists

def manhattan(list):
    localList = list[:]
    hValue = 0

    Dict = {'coord1': [0,0], 'coord2': [0,1], 'coord3': [0,2],
            'coord4': [1,0], 'coord5': [1,1], 'coord6': [1,2],
            'coord7': [2,0], 'coord8':[2,1]}

    for x in range(1,9):

        if localList.index(x) == 0:
            actual = [0,0]
        elif localList.index(x) == 1:
            actual = [0,1]
        elif localList.index(x) == 2:
            actual = [0,2]
        elif localList.index(x) == 3:
            actual = [1,0]
        elif localList.index(x) == 4:
            actual = [1,1]
        elif localList.index(x) == 5:
            actual = [1,2]
        elif localList.index(x) == 6:
            actual = [2,0]
        elif localList.index(x) == 7:
            actual = [2,1]
        elif localList.index(x) == 8:
            actual = [2,2]

        string = 'coord' + str(x)

        coord = Dict[string]


        h = (abs(actual[0] - coord[0]) + abs(actual[1] - coord[1]))


        hValue = hValue + h

    return hValue

def solve(list):
    #localvariables
    g = 0
    h = 0
    workingList = list[:]
    h = manhattan(workingList)
    pq = []
    f = h+g
    openList = []
    closedList = []
    currentList = []
    closedIndex = 0

    FINALLIST=[]

    heapq.heappush(pq,(f, workingList, (g, h, -1)))
    workingList = heapq.heappop(pq)
    checklist = []
    #print(localList, 'h={}'.format(h), ' moves={}'.format(g))
    while True:
        #only used to find current state succesors
        currentLists = succ(workingList[1])

        #pushes all of the succesors into the queue
        for x in currentLists:
            #pq is the heap, h is manhattan(x), g is the previous moves plus this move, parent index is the previous
            heapq.heappush(pq,((manhattan(x) + (workingList[2][0]+1)), x, ((workingList[2][0]+1),manhattan(x), closedIndex)))

        #puts expanded list into closed list
        closedList.append(workingList)
        closedIndex = closedIndex+1

        #sets the workinglist to what was popped
        workingList = heapq.heappop(pq)

        #if the state of what was popped in is the closed list then we pop somthing else
        #if workingList[1] in closedList:
            #workingList = heapq.heappop(pq)


        #get the correct tuples into finallist when workinglist becomes 123456780
        if workingList[1] == [1,2,3,4,5,6,7,8,0]:
            while True:
                #print(workingList[1], 'h=', workingList[2][1], 'moves:', workingList[2][0])
                FINALLIST.append(workingList)
                workingList = closedList[workingList[2][2]]
                if workingList[2][0] == 0:
                    FINALLIST.append(workingList)
                    #print(workingList[1], 'h=', workingList[2][1], 'moves:', workingList[2][0])
                    break
            break
        print(workingList[1])
    #PRINGTING CORRECT OUTPUT
    FINALLIST.reverse()
    for list in FINALLIST:
        print(list[1], 'h={}'.format(list[2][1]), 'moves: {}'.format(list[2][0]))






#solve([1,2,3,4,5,6,7,0,8])
#solve([8, 6, 7, 2, 5, 4, 3, 0, 1])
#print_succ([8,7,6,5,4,3,2,1,0])
#print_succ([1,2,3,4,5,0,6,7,8])
solve([4,1,8,5,3,6,2,7,0])
#h([1, 2, 3, 4, 5, 8, 6, 7, 0])
