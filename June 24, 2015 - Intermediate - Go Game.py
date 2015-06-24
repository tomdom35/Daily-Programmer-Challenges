def getLines():
    file = open(r'C:\Users\1020071\Desktop\info.txt','r')
    lines = []
    for line in file:
        lines.append(line)
    return lines

def formatLines(lines, width):
    formattedLines = []
    formattedLine = ""
    for line in lines:
        for x in range(0,width):
            formattedLine+=line[x]
        formattedLines.append(formattedLine)
        formattedLine = ""
    return formattedLines

def printBoard(lines):
    for line in lines:
        print(line)
    
lines = getLines()
firstLine = lines[0].split()
width = int(firstLine[0])
height = int(firstLine[1])
color = (lines[1])[0]
lines.pop(0)
lines.pop(0)
print('Width: ',width)
print('Height: ',height)
print('Color: ',color)
print()
lines = formatLines(lines,width)
printBoard(lines)
print()
print(lines)
groups = []
groups.append([(1,2),(2,3)])
print(groups)
