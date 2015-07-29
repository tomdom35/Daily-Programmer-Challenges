dictionary = open('words.txt')
poem = open('poem.txt')
possibleLines = []
words = dictionary.read().splitlines()
poemLines = poem.read().splitlines()
for index in range(0,len(words)):
    words[index] = words[index].lower()
def findLines(poemLines,words,index):
    possibleLines = []
    for line in poemLines:
        newLine = line.split()
        newLineLength = len(newLine)
        if not (index>newLineLength-1):
            word = newLine[index]
        else:
            word = newLine[newLineLength-1]
        length = len(word)
        if not (word[length-1].isalpha()):
            word = word[:-1]
        if word in words:
            possibleLines.append(line)
    print (len(possibleLines))
    if(len(possibleLines)!=len(poemLines)):
        findLines(possibleLines,words,index+1)
    else:
        for line in possibleLines:
            print(line)
findLines(poemLines,words,0)
