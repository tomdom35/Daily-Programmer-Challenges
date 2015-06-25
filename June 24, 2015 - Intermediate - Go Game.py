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

def inGroup(groups,lineLetter):
    for group in groups:
        if lineLetter in group:
            return True
    return False

def createGroup(groups, groupSpaces, lines, line, letter, width, height):
    if(letter<width-1 and lines[line][letter] == lines[line][letter+1] and not(inGroup(groups,(line,letter+1)))):
        groups[len(groups)-1].append((line,letter+1))
        createGroup(groups, groupSpaces, lines, line, letter+1, width, height)
    if(letter>0 and lines[line][letter] == lines[line][letter-1] and not(inGroup(groups,(line,letter-1)))):
        groups[len(groups)-1].append((line,letter-1))
        createGroup(groups, groupSpaces, lines, line, letter-1, width, height)
    if(line<height-1 and lines[line][letter] == lines[line+1][letter] and not(inGroup(groups,(line+1,letter)))):
        groups[len(groups)-1].append((line+1,letter))
        createGroup(groups, groupSpaces, lines, line+1, letter, width, height)
    if(line>0 and lines[line][letter] == lines[line-1][letter] and not(inGroup(groups,(line-1,letter)))):
        groups[len(groups)-1].append((line-1,letter))
        createGroup(groups, groupSpaces, lines, line-1, letter, width, height)


lines = getLines()
firstLine = lines[0].split()
width = int(firstLine[0])
height = int(firstLine[1])
myColor = (lines[1])[0]
otherColor = ""
if(myColor == 'w'):
    otherColor = 'b'
else:
    otherColor = 'w'
lines.pop(0)
lines.pop(0)
print('Width: ',width)
print('Height: ',height)
print('Color: ',myColor)
print()
lines = formatLines(lines,width)
printBoard(lines)
print()
groups = []
groupSpaces = []
for line in range(0,height):
    for letter in range(0,width):
        if(lines[line][letter] == otherColor and not(inGroup(groups,(line,letter)))):
            groups.append([(line,letter)])
            groupSpaces.append([])
            createGroup(groups, groupSpaces, lines, line, letter, width, height)
print(groups)
