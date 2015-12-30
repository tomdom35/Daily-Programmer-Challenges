grid = []
height = 0
width = 0
xLoc = []
with open('grid.txt') as file:
    line = file.readline().rstrip()
    width = int(line[:line.index(',')])
    height = int(line[line.index(' ')+1:])
    l = 0
    for line in file:
        row = list(line.rstrip())
        grid.append(row)
        while 'X' in row:
            xLoc.append((l,row.index('X')))
            row[row.index('X')] = 'x'
        l+=1

def radixSort(xLoc,index,bucketSize):
    buckets = []
    for x in range(bucketSize[index]):
        buckets.append([])
    for x in xLoc:
        buckets[x[index]].append(x)
    buckets = [j for i in buckets for j in i]
    buckets.reverse()
    if(index==1):
        return radixSort(buckets,0,bucketSize)
    else:
        return buckets

def numPaths(n1,n2):
    if(n1 == n2):
        return 1
    totalPaths = 0
    nextNodes = []
    if(n1[0]==n2[0]):
        nextNodes.append((n1[0],n1[1]+1))
    elif(n1[1]==n2[1]):
        nextNodes.append((n1[0]-1,n1[1]))
    elif(n1[0]>=n2[0] and n1[1]<=n2[1]):
        nextNodes.append((n1[0],n1[1]+1))
        nextNodes.append((n1[0]-1,n1[1]))
        nextNodes.append((n1[0]-1,n1[1]+1))
    for n in nextNodes:
        totalPaths += numPaths(n,n2)
    return totalPaths

def totalPaths(x):
    xLoc = radixSort(x,1,(height,width))
    totalPaths = 1
    for i in range(1,len(xLoc)):
        totalPaths*=numPaths(xLoc[i-1],xLoc[i])
    return totalPaths

print("Number of paths:",totalPaths(xLoc))
