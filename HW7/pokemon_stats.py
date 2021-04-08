    import csv
import math
import numpy

def load_data(filepath):
    dataset = []
    workingDict = {}
    with open(filepath, newline= '') as csvfile:
        reader = csv.DictReader(csvfile)
        i = 1
        for row in reader:
            if i > 20:
                break
            workingDict[i] = {'#': int(row['#']), 'Name': row['Name'], 'Type 1': row['Type 1'], 'Type 2': row['Type 2'], 'Total': int(row['Total']), 'HP': int(row['HP']), 'Attack': int(row['Attack']), 'Defense': int(row['Defense']), 'Sp. Atk': int(row['Sp. Atk']), 'Sp. Def': int(row['Sp. Def']), 'Speed': int(row['Speed'])}
            i += 1
    for x in range(1,21):
        dataset.append(workingDict[x])

    #print(workingDict)
    return dataset

def calculate_x_y(stats):
    offensive = int(stats['Attack']) + int(stats['Sp. Atk']) + int(stats['Speed'])
    defensive = int(stats['Defense']) + int(stats['Sp. Def']) + int(stats['HP'])

    tuple = (offensive, defensive)

    return tuple

def pointDistanceCheck(p1, p2):
    distance = math.sqrt( ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2) )
    return distance
def clusterDistanceCheck(cluster1, cluster2):
    #comparing clusters with one point
    if len(cluster1) == 2 and len(cluster2) == 2:
        P1 = list(cluster1)
        P2 = list(cluster2)
        distance = pointDistanceCheck(P1, P2)
        numPoints = 2
        combinedList = P1 + P2
        merged = tuple(combinedList)
        rList = [distance, numPoints, merged]
        return rList
    #comparing clusters with not 1 and 1 points
    else:
        P1 = list(cluster1)
        P2 = list(cluster2)
        combinedList = P1 + P2
        cluster1Points = {}
        cluster2Points = {}
        tempCheck = []
        pointIndex = 0
        #making cluster points from the lists
        for x in range(len(P1)):
            if x % 2 == 0:
                point = [P1[x], P1[x+1]]
                cluster1Points[pointIndex] = point
                pointIndex += 1
        pointIndex = 0
        for x in range(len(P2)):
            if x % 2 == 0:
                point = [P2[x], P2[x+1]]
                cluster2Points[pointIndex] = point
                pointIndex += 1
        #iterating through points
        i = 0
        for x in range(len(cluster1Points)):
            for y in range(len(cluster2Points)):
                i += 1
                distance = pointDistanceCheck(cluster1Points[x], cluster2Points[y])
                tempCheck.append(distance)

        distance = min(tempCheck)
        numPoints = ((len(P1) + len(P2)) / 2)
        merged = tuple(combinedList)
        rList = [distance, numPoints, merged]
        return rList

def hac(dataset):
    #putting tuples into dict to track original cluster numberrs
    oClusterDict = {}
    for x in range(0,20):
        oClusterDict[x] = dataset[x]

    #creating (m-1)x4 array
    finalArray = []
    tempCheck = {}
    for i in range(1, 21):
        finalArray.append([0,0,0,0])
    #clustering...
    m = 0
    iteration = 0
    while iteration<19:
        iteration += 1
        #making all the comparisons
        lowestDistance = 10000000
        for k in oClusterDict:
            for key in oClusterDict:
                if k != key:
                    tempCheck[m] = [clusterDistanceCheck(oClusterDict[k], oClusterDict[key]), k, key]
                    #checking to see if distance returned is the lowest so far if it is we save values
                    if tempCheck[m][0][0] < lowestDistance:
                        lowestDistance = tempCheck[m][0][0]
                        first = k
                        second = key
                        totalPoints = tempCheck[m][0][1]
                        mergedCluster = tempCheck[m][0][2]
                    m += 1
        #swapping indecies if second is bigger than first
        if second < first:
            tqqq = first
            first = second
            second = tqqq

        #SETTING final array row
        finalArray[iteration][0] = first
        finalArray[iteration][1] = second
        finalArray[iteration][2] = lowestDistance
        finalArray[iteration][3] = totalPoints

        #adding newcluster to oClusterDict
        oClusterDict[19+iteration] = mergedCluster

        #removing from oClusterDict
        oClusterDict.pop(first)
        oClusterDict.pop(second)
        #print(oClusterDict)
        #print(finalArray[iteration])
        #print(tempCheck)

    # idk why i had to put this here but my iteration was messed up i guess
    finalArray.pop(0)
    print(finalArray)
    return numpy.array(finalArray)








stats = load_data(r'C:\Users\Owner\Documents\Atom\CS540\HW7\Pokemon.csv')
#print(stats[0])
#print(calculate_x_y(stats[0]))
listOfTuples = []
for stat in stats:
    listOfTuples.append(calculate_x_y(stat))

hac(listOfTuples)
#print(clusterDistanceCheck((159,159,202,203), (262,263,302,323)))
