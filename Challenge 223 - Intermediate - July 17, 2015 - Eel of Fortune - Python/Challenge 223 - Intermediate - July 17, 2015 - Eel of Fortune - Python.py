def problem(secretWord, offensiveWord):
    index = -1
    num = -1
    for letter in offensiveWord:
        num += 1
        if letter in secretWord:
            if offensiveWord.count(letter) == secretWord.count(letter):
                try:
                    newIndex = secretWord.index(letter, index+1)
                    index = newIndex
                except ValueError:
                    return False
                if(num == len(offensiveWord)-1):
                    return True
            else:
                return False
        else:
            return False
    return False

def increment(checkWord, index):
    tempWord = list(checkWord)
    letter = tempWord[index]
    if(ord(letter) == 122):
        if(index+1 <len(tempWord)):
            tempWord[index] = 'a'
            checkWord = ''.join(tempWord)
            return increment(checkWord, index+1)
        else:
            return checkWord
    else:
        tempWord[index] = chr(ord(letter)+1)
        return ''.join(tempWord)


file = open('enable1.txt')
lines = file.readlines()
words = []
for line in lines:
    if(len(line) >= 5):
        words.append(line)


#Challenge One
count = 0
for line in lines:
    if problem(line,'rrizi'):
        count += 1
print('The problem count of \'rrizi\' is:',count)
print()

#Challenge Two
checkWord = 'aaaaa'
finalCount = 26**len(checkWord)
currentCount = 0
maxProblemCount = 0
maxProblemCountWord = ''

print('Finding largest 5 character string problem count...')
while(currentCount<finalCount):
    tempProblemCount = 0
    print('%f' % (currentCount/finalCount), '%', sep='')
    for word in words:
        if problem(word,checkWord):
            tempProblemCount += 1
    if tempProblemCount > maxProblemCount:
        maxProblemCountWord = checkWord
        maxProblemCount = tempProblemCount
    checkWord = increment(checkWord,0)
    currentCount += 1

print(maxProblemCountWord)
print(maxProblemCount)
