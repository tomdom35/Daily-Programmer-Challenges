def getLines():
    file = open('info.txt','r')
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
    if(letter<width-1):
        if (lines[line][letter] == lines[line][letter+1] and not(inGroup(groups,(line,letter+1)))):
            groups[len(groups)-1].append((line,letter+1))
            createGroup(groups, groupSpaces, lines, line, letter+1, width, height)
        elif(lines[line][letter+1] == ' '):
            groupSpaces[len(groupSpaces)-1].append((line,letter+1))
            
    if(letter>0):
        if(lines[line][letter] == lines[line][letter-1] and not(inGroup(groups,(line,letter-1)))):
            groups[len(groups)-1].append((line,letter-1))
            createGroup(groups, groupSpaces, lines, line, letter-1, width, height)
        elif(lines[line][letter-1] == ' '):
            groupSpaces[len(groupSpaces)-1].append((line,letter-1))
            
    if(line<height-1):
        if(lines[line][letter] == lines[line+1][letter] and not(inGroup(groups,(line+1,letter)))):
            groups[len(groups)-1].append((line+1,letter))
            createGroup(groups, groupSpaces, lines, line+1, letter, width, height)
        elif(lines[line+1][letter] == ' '):
            groupSpaces[len(groupSpaces)-1].append((line+1,letter))
    if(line>0):
        if(lines[line][letter] == lines[line-1][letter] and not(inGroup(groups,(line-1,letter)))):
            groups[len(groups)-1].append((line-1,letter))
            createGroup(groups, groupSpaces, lines, line-1, letter, width, height)
        elif(lines[line-1][letter] == ' '):
            groupSpaces[len(groupSpaces)-1].append((line-1,letter))

def removeDuplicates(groups):
    for group in groups:
        for item in group:
            while(group.count(item)>1):
                group.remove(item)

def combineGroups(groups, groupSpaces):
    for group in groupSpaces:
        while(groupSpaces.count(group)>1):
            tempIndex = groupSpaces.index(group)
            groupSpaces.remove(group)
            newIndex = groupSpaces.index(group)
            tempGroup = groups[tempIndex]
            groups.remove(tempGroup)
            groups[newIndex].extend(tempGroup)

def findRemovalPoint(groups, groupSpaces):
    largestGroup = 0
    removalPoint = (-1,-1)
    for index in range(0,len(groups)):
        if(len(groupSpaces[index]) == 1 and len(groups[index])>largestGroup):
            removalPoint = (groupSpaces[index][0][1],groupSpaces[index][0][0])
            largestGroup = len(groups[index])
    return removalPoint

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
print('My Color: ',myColor)
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
removeDuplicates(groupSpaces)
combineGroups(groups, groupSpaces)
removalPoint = findRemovalPoint(groups, groupSpaces)
if(removalPoint == (-1,-1)):
    removalPoint = "No constructive move"
print('Removal Point: ',removalPoint)
