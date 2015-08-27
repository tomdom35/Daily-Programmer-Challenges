def findX(gird):
    row = -1
    col = -1
    for line in grid:
        if 'x' in line:
            return (grid.index(line),line.index('x'))
    return (row,col)

def countChain(grid,row,col,rows,cols):
    grid[row][col] = ' '
    if(row+1<rows and grid[row+1][col] == 'x'):
        countChain(grid,row+1,col,rows,cols)
    if(row-1>=0 and grid[row-1][col] == 'x'):
        countChain(grid,row-1,col,rows,cols)
    if(col+1<cols and grid[row][col+1] == 'x'):
        countChain(grid,row,col+1,rows,cols)
    if(col-1>=0 and grid[row][col-1] == 'x'):
        countChain(grid,row,col-1,rows,cols)

file = open('chains.txt')
info = file.readline()
rows = int(info[:info.index(' ')])
cols = int(info[info.index(' ')+1:])
grid = []
for line in file:
    grid.append(list(line))

row = findX(grid)[0]
col = findX(grid)[1]
numChains = 0
while((row,col) != (-1,-1)):
    countChain(grid,row,col,rows,cols)
    numChains+=1
    row = findX(grid)[0]
    col = findX(grid)[1]

print(numChains)
    
