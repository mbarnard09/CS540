import numpy as np
import random
import csv
import statistics

# Feel free to import other packages, if needed.
# As long as they are supported by CSL machines.


def get_dataset(filename):
    """
    TODO: implement this function.

    INPUT:
        filename - a string representing the path to the csv file.

    RETURNS:
        An n by m+1 array, where n is # data points and m is # features.
        The labels y should be in the first column.
    """
    dataset = []
    workingDict = []
    with open(filename, newline= '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            workingDict.append(float(row['BODYFAT']))
            workingDict.append(float(row['DENSITY']))
            workingDict.append(float(row['AGE']))
            workingDict.append(float(row['WEIGHT']))
            workingDict.append(float(row['HEIGHT']))
            workingDict.append(float(row['ADIPOSITY']))
            workingDict.append(float(row['NECK']))
            workingDict.append(float(row['CHEST']))
            workingDict.append(float(row['ABDOMEN']))
            workingDict.append(float(row['HIP']))
            workingDict.append(float(row['THIGH']))
            workingDict.append(float(row['KNEE']))
            workingDict.append(float(row['ANKLE']))
            workingDict.append(float(row['BICEPS']))
            workingDict.append(float(row['FOREARM']))
            workingDict.append(float(row['WRIST']))
            dataset.append(workingDict)
            workingDict = []
        return np.array(dataset)


def print_stats(dataset, col):
    """
    TODO: implement this function.

    INPUT:
        dataset - the body fat n by m+1 array
        col     - the index of feature to summarize on.
                  For example, 1 refers to density.

    RETURNS:
        None
    """
    rowCount = 0
    meanCount = 0
    SDlist = []
    for row in dataset:
        rowCount += 1
        for c in range(len(row)):
            if c == 1:
                meanCount = float(row[c]) + meanCount
                SDlist.append(float(row[c]))
    sd = statistics.stdev(SDlist)


    mean = meanCount/rowCount
    print(rowCount)
    print(round(mean, 2))
    print(round(sd,2))



def regression(dataset, cols, betas):
    """
    TODO: implement this function.

    INPUT:
        dataset - the body fat n by m+1 array
        cols    - a list of feature indices to learn.
                  For example, [1,8] refers to density and abdomen.
        betas   - a list of elements chosen from [beta0, beta1, ..., betam]

    RETURNS:
        mse of the regression model
    """
    mse = 0
    xValueDict = {}
    temp = 0
    rowCount = 0
    for row in dataset:
        rowCount += 1
        for x in range(len(cols)):
            for c in range(len(row)):
                if c == cols[x]:
                    xValueDict[x] = float(row[c])
                elif c == 0:
                    yValue = float(row[c])
        #have collected x values and y value for the row, now calculate sum for row
        sumRow = 0
        tempSumRow = 0
        #calculating all Bi*Xi values
        for y in range(len(betas)):
            if y == 0:
                tempSumRow = betas[y]
            else:
                tempSumRow = betas[y] * xValueDict[y-1]
            sumRow += tempSumRow
        #subtracting the yValue from the Bi*Xi value for the row
        sumRow = sumRow - yValue
        sumRow = sumRow * sumRow

        #adding the row value to the total value
        mse += sumRow
    return mse/rowCount


def gradient_descent(dataset, cols, betas):
    """
    TODO: implement this function.

    INPUT:
        dataset - the body fat n by m+1 array
        cols    - a list of feature indices to learn.
                  For example, [1,8] refers to density and abdomen.
        betas   - a list of elements chosen from [beta0, beta1, ..., betam]

    RETURNS:
        An 1D array of gradients
    """
    grads = []
    xValueDict = {}
    temp = 0
    tempGrad = 0
    rowCount = 0
    for Xi in range(len(cols)+1):
        for row in dataset:
            rowCount += 1
            for x in range(len(cols)):
                for c in range(len(row)):
                    if c == cols[x]:
                        xValueDict[x] = float(row[c])
                    elif c == 0:
                        yValue = float(row[c])
            #have collected x values and y value for the row, now calculate sum for
            #row and add to gradient list
            sumRow = 0
            tempSumRow = 0
            #calculating all Bi*Xi values
            for y in range(len(betas)):
                if y == 0:
                    tempSumRow = betas[y]
                else:
                    tempSumRow = betas[y] * xValueDict[y-1]
                sumRow += tempSumRow
            #subtracting the yValue from the Bi*Xi value for the row
            sumRow = (sumRow - yValue)

            #part changed per col in cols list passsed in
            if Xi == 0:
                tempGrad += sumRow
            else:
                tempGrad += sumRow * xValueDict[Xi - 1]
                #grads.append(tempGrad * (2/rowCount))
                #tempGrad += sumRow * xValueDict[0]
        grads.append(tempGrad * (2/rowCount))
        tempGrad =0
        xValueDict = {}
        temp = 0
        tempGrad = 0
        rowCount = 0



    return grads


def iterate_gradient(dataset, cols, betas, T, eta):
    """
    TODO: implement this function.

    INPUT:
        dataset - the body fat n by m+1 array
        cols    - a list of feature indices to learn.
                  For example, [1,8] refers to density and abdomen.
        betas   - a list of elements chosen from [beta0, beta1, ..., betam]
        T       - # iterations to run
        eta     - learning rate

    RETURNS:
        None
    """
    betaDict = {}
    #setting up betaDisct with original beta values
    for x in range(len(betas)):
        betaDict[x] = betas[x]
    #getting betas for first iteration
    betaList = []
    #have to first set up beta list to pass in to gradient_descent
    for x in range(len(betaDict)):
        betaList.append(betaDict[x])

    betaReturnedList = gradient_descent(dataset, cols, betaList)
    #getting new betas for first iteration
    for y in range(len(betaDict)):
        betaDict[y] = betaDict[y] - (betaReturnedList[y]*eta)

    for h in range(len(betaDict)):
        betaList[h] = betaDict[h]
    MSE = regression(dataset, cols, betaList)
    ###########################################################################
    printStr = ''
    #T=1 is already set up
    for iteration in range(1, (T+1)):
        #adding all betas to a string to be printed
        for L in range(len(betaDict)):
            printStr += str('{:.2f} '.format(betaDict[L]))
        #printing
        print('{} {:.2f} {}'.format(iteration, MSE, printStr))
        ###Clearing Variables##################
        printStr = ''
        #betaDict = {}
        betaList = []
        betaReturnedList = []
        ######setting up next iteration########
        #list to be passed in to gradient
        for x in range(len(betaDict)):
            betaList.append(betaDict[x])

        betaReturnedList = gradient_descent(dataset, cols, betaList)
        #getting new betas for next iteration
        for y in range(len(betaDict)):
            betaDict[y] = betaDict[y] - (betaReturnedList[y]*eta)
        #getting MSE for next iteration
        for p in range(len(betaDict)):
            betaList[p] = betaDict[p]
        MSE = regression(dataset, cols, betaList)


def compute_betas(dataset, cols):
    """
    TODO: implement this function.

    INPUT:
        dataset - the body fat n by m+1 array
        cols    - a list of feature indices to learn.
                  For example, [1,8] refers to density and abdomen.

    RETURNS:
        A tuple containing corresponding mse and several learned betas
    """
    betas = None
    mse = None
    matrix = []
    matrixRow =[1]
    yMatrix = []
    yMatrixRow = []
    #each row of dataset
    for row in dataset:
        #each col in row
        for x in range(len(row)):
            if x == 0:
                yMatrixRow.append(float(row[x]))
            #0,1
            for y in range(len(cols)):
                if x == cols[y]:
                    matrixRow.append(float(row[y+1]))
        matrix.append(matrixRow)
        yMatrix.append(yMatrixRow)
        matrixRow = [1]
        yMatrixRow = []

    yMatrix = np.array(yMatrix)
    matrix = np.array(matrix)
    trans = np.transpose(matrix)
    inv = np.linalg.inv(np.matmul(trans,matrix))

    result1 = np.matmul(inv,trans)

    result = np.matmul(result1, yMatrix)

    betaList = []

    for r in range(len(result)):
        betaList.append(result[r][0])
    #end = yMatrix.dot(end)

    transpose = 0

    MSE = regression(dataset, cols, betaList)

    betaList.insert(0,MSE)
    #print(betaList)
    betaTuple = tuple(betaList)
    return (betaTuple)


def predict(dataset, cols, features):
    """
    TODO: implement this function.

    INPUT:
        dataset - the body fat n by m+1 array
        cols    - a list of feature indices to learn.
                  For example, [1,8] refers to density and abdomen.
        features- a list of observed values

    RETURNS:
        The predicted body fat percentage value
    """
    result = 0

    betas = compute_betas(dataset, cols)
    betaList = []
    for x in range(1,len(betas)):
        betaList.append(betas[x])

    #print(betaList)

    tempResult = 0
    for x in range(len(betaList)):
        if x == 0:
            result += betaList[x]
        else:
            result += betaList[x]*features[x-1]

    return result


def random_index_generator(min_val, max_val, seed=42):
    """
    DO NOT MODIFY THIS FUNCTION.
    DO NOT CHANGE THE SEED.
    This generator picks a random value between min_val and max_val,
    seeded by 42.
    """
    random.seed(seed)
    while True:
        yield random.randrange(min_val, max_val)


def sgd(dataset, cols, betas, T, eta):
    """
    TODO: implement this function.
    You must use random_index_generator() to select individual data points.

    INPUT:
        dataset - the body fat n by m+1 array
        cols    - a list of feature indices to learn.
                  For example, [1,8] refers to density and abdomen.
        betas   - a list of elements chosen from [beta0, beta1, ..., betam]
        T       - # iterations to run
        eta     - learning rate

    RETURNS:
        None
    """
    pass

