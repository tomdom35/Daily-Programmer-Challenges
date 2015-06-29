class Dictionary:
    def __init__(self, fileName):
        file = open(fileName)
        self.words = file.read().splitlines()

    def containsWord(self, word):
        if word in self.words:
            return True
        else:
            return False

    def findPossibleWords(self, text):
        possibleWords = []
        for word in self.words:
            match = False
            if(len(word) == len(text)):
                match = True
                for index in range(0,len(word)):
                    if not(text[index].isupper()): 
                        if text[index] != word[index]:
                            match = False
            if match:
                possibleWords.append(word)
        return possibleWords

def createKey(info):
    key = []
    print('===Key===')
    for hint in info:
        print(hint[0], '--->' ,hint[1])
        key.append((hint[0],hint[1]))
    print()
    return key

def useKey(cipherText, key):
    for word in cipherText:
        for hint in key:
            if hint[1] in word:
                index = cipherText.index(word)
                word = word.replace(hint[1],hint[0])
                cipherText[index] = word
    print('Cipher Text After Key :', cipherText, '\n')

def checkWordsWithSameLetter(myWord, cipherText, possiblePlainText):
    for letterIndex in range(0,len(myWord)):
        checkList = []
        letter = myWord[letterIndex]
        for wordIndex in range(0,len(cipherText)):
            word = cipherText[wordIndex]
            if word!= myWord:
                if letter in word:
                    letterIndex2 = word.index(letter)
                    if (cipherText.index(myWord),letterIndex) not in checkList:
                        checkList.append((cipherText.index(myWord),letterIndex))
                    if (wordIndex,letterIndex2) not in checkList:
                        checkList.append((wordIndex,letterIndex2))
        for item in checkList:
            updatePlainText(item, checkList, possiblePlainText)

def updatePlainText(item, checkList, possiblePlainText):
    for element in checkList:
        newList1 = []
        newList2 = []
        if element != item:
            for word1 in possiblePlainText[item[0]]:
                found = False
                for word2 in possiblePlainText[element[0]]:
                    if word1[item[1]] == word2[element[1]]:
                        found = True
                if not found:
                    possiblePlainText[item[0]].remove(word1)

def updateKey(key, word, cipherText):
    updated = False
    for index in range(0,len(word)):
        if cipherText[index].isupper():
            if (word[index],cipherText[index]) not in key:
                key.append((word[index],cipherText[index]))
                updated = True
    return updated

def decoded(possiblePlainText):
    for words in possiblePlainText:
        if len(words) != 1:
            return False
    return True
            
dictionary = Dictionary('words.txt')
info = open('input.txt').read().splitlines()
cipherText = info[0].split()
print('Original Cipher Text: ', info[0], '\n')
info = info[2:]
key = createKey(info)
useKey(cipherText, key)
done = False
while not done:
    keyUpdated = False
    possiblePlainText = []
    for word in cipherText:
        possiblePlainText.append(dictionary.findPossibleWords(word))
    for x in range(0,2):
        for word in cipherText:
            for x in range(0,len(cipherText)):checkWordsWithSameLetter(word, cipherText, possiblePlainText)
    for index in range(0,len(possiblePlainText)):
        if len(possiblePlainText[index]) == 1:
            keyUpdated = updateKey(key,possiblePlainText[index][0],cipherText[index])
    if keyUpdated: useKey(cipherText, key)
    complete = decoded(possiblePlainText)
    done = (not(keyUpdated) and not(complete)) or complete
for words in possiblePlainText:
    print(len(words),'possibilities for',cipherText[possiblePlainText.index(words)])
            
