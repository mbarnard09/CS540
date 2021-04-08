def fill(state, max, which):
    localList = state[:]
    localList[which] = max[which]
    return localList

def xfer(state, max, source, dest):
    localList = state[:]
    #WHILE DEST ISNT OVER MAX VALUE AND SOURCE ISNT BELOW ZERO WE WILL KEEP
    #INCREASING/DECREASING THE VALUES OF THE TWO
    while localList[dest] < max[dest] and localList[source] > 0:
        localList[dest] += 1
        localList[source] -= 1
    return localList
def empty(state, max, which):
    localList = state[:]
    localList[which] = 0
    return localList

def succ(state, max):
    localList = state[:]
    s1 = empty(localList, max, 0)
    s2 = empty(localList, max, 1)
    s3 = fill(localList, max, 0)
    s4 = fill(localList, max, 1)
    s5 = xfer(localList,max,0,1)
    s6 = xfer(localList,max,1,0)

    final = []
    #PRINT 1 BY DEFAULT AND THEN COMPARE EVERYTIME AFTER
    final.append(s1)

    if s2 == s1:
        pass
    else:
        final.append(s2)

    if s3 == s1 or s3 == s2:
        pass
    else:
        final.append(s3)
    if s4 == s1 or s4 == s2 or s4 == s3:
        pass
    else:
        final.append(s4)
    if s5 == s1 or s5 == s2 or s5 == s3 or s5 == s4:
        pass
    else:
        final.append(s5)
    if s6 == s1 or s6 == s2 or s6 == s3 or s6 == s4 or s6 == s5:
        pass
    else:
        final.append(s6)
    print(final)
#testing
#max = [5,7]
#s0 = [0,0]
#print (fill(s0, max,1))
#print(s0)
#print (fill(s0, max, 0))
#s1 = fill(s0,max,1)
#print(xfer(s1,max,1,0))
#print("\n")
#succ(s0, max)
#print("\n")
#s0 = [3,1]
#succ(s0, max)
#fill(state, max, which)
#empty(state, max, which)
#xfer(state, max, source, dest)
#succ(state, max)

#s0 = [0,0]
#max = [3,7]
#print(empty(s0,max,1))
#print(s0 == empty(s0,max,1))
