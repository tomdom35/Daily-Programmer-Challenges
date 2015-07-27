import sys

def printRectangles(row,numCol,symbolPoints):
    index = 0
    for r in range(0,row):
        for c in range(0,numCol[r]):
            sys.stdout.write(symbols[index])
            index += 1
        print()

def getSymbol(point,points,symbols):
    if point in points:
        index = points.index(point)
        symbol = symbols[index]
    else:
        symbol = '?'
    return symbol

def checkLeft(r,c,points,symbols):
    numSquares = 0
    row = r
    col = c
    while(getSymbol((row,col - 1),points,symbols) == '-' or getSymbol((row,col - 1),points,symbols) == '+'):
        if(getSymbol((row,col - 1),points,symbols) == '+'):
            numSquares += checkDown(row,col-1,points,symbols,c,r)
        col -= 1
    return numSquares

def checkDown(r,c,points,symbols,endCol,endRow):
    numSquares = 0
    row = r
    col = c
    while(getSymbol((row+1,col),points,symbols) == '|' or getSymbol((row+1,col),points,symbols) == '+'):
        if(getSymbol((row+1,col),points,symbols) == '+'):
            numSquares += checkRight(row+1,col,points,symbols,endCol,endRow)
        row += 1
    return numSquares

def checkRight(r,c,points,symbols,endCol,endRow):
    numSquares = 0
    row = r
    col = c
    while((getSymbol((row,col + 1),points,symbols) == '-' or getSymbol((row,col + 1),points,symbols) == '+') and col<endCol):
        if(getSymbol((row,col + 1),points,symbols) == '+' and col+1 == endCol):
            numSquares += checkUp(row,col+1,points,symbols,endRow)
        col += 1
    return numSquares

def checkUp(r,c,points,symbols,endRow):
    row = r
    col = c
    while((getSymbol((row - 1,col),points,symbols) == '|' or getSymbol((row - 1,col),points,symbols) == '+') and row>endRow):
        if(getSymbol((row - 1,col),points,symbols) == '+' and row-1 == endRow):
            return 1
        row -= 1
    return 0

file = open('rectangle.txt')
symbols = []
points = []
row = 0
col = 0
numCol = []
for line in file:
    col = 0
    for char in line:
        if line.index(char)<len(line)-1:
            points.append((row,col))
            symbols.append(char)
            col += 1
    numCol.append(col)
    row += 1

index = 0
numSquares = 0
for r in range(0,row):
    for c in range(0,numCol[r]):
        if getSymbol((r,c),points,symbols) == '+':
            numSquares += checkLeft(r,c,points,symbols)
        index+=1
print(numSquares)
