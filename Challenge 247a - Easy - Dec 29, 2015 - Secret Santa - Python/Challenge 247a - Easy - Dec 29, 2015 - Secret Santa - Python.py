names = []
taken = []
with open('names.txt') as file:
    for line in file:
        names.append(line.rstrip().split(' '))

for name in names:
    innerIndex = 0
    index = names.index(name)+1
    if(index>=len(names)):
        index = 0
    for i in name:
        while(names[index][innerIndex] in taken):
            if(innerIndex<len(names[index])-1):
                innerIndex+=1
            else:
                innerIndex = 0
                index+=1
                if(index>=len(names)):
                   index = 0
        print(i,'-->',names[index][innerIndex])
        taken.append(names[index][innerIndex])
