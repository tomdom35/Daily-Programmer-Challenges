import sys

def createBoard(col, row):
    board = []
    for i in range(0,col):
        r = []
        for j in range(0,row):
            r.append(0)
        board.append(r)
    return board

def printBoard(board,col,row):
    sys.stdout.write(' ')
    for c in range(0,col):
        sys.stdout.write(' ' + chr(65+c))
    print()
    for i in range(0,row):
        sys.stdout.write(str(i+1) + ' ')
        for j in range(0,col):
            sys.stdout.write(str(board[j][i]) + ' ')
        print()

def checkDuplicates(l):
    for i in l:
        if l.count(i) > 1:
            return True
    return False

def findNums(num,n):
    nums = []
    checkNums = []
    count = 0
    d = 9
    s = 0
    for i in range(0,n):
        checkNums.append(i+1)
        s += d-i
    startNums = []+checkNums
    index = len(checkNums) - 1
    while(sum(checkNums)<s):
        if(sum(checkNums)==num):
            if sorted(checkNums) not in nums:
                if(not checkDuplicates(checkNums)):
                    nums.append([]+sorted(checkNums))
        if(checkNums[index] == 9):
            checkNums[index] = startNums[index]
            startNums[index] = startNums[index] + 1 if startNums[index]<9 else startNums[index]
            if(index==0):
                index=len(checkNums) - 1
                checkNums[index] = startNums[index]
            else:
                index-=1
                checkNums[index]+=1
        else:
            checkNums[index]+=1
    return nums

def getNumList(puzzle):
    numList = []
    for i in puzzle:
        numList.append(findNums(i[0],len(i)-1))
    return numList

file = open('kakuro.txt')
line = file.readline()
col = int(line[0])
row = int(line[2])
puzzle = []
for line in file:
    x = line.split()
    x[0] = int(x[0])
    puzzle.append(x)
board = createBoard(col,row)
printBoard(board,col,row)
numList = getNumList(puzzle)
for i in range(0,len(puzzle)):
    print(puzzle[i][0])
    print(numList[i])
