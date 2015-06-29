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
    for word in cipherText:
        if word != myWord:
            for letter in myWord:
                if letter in word:
                    index1 = myWord.index(letter)
                    index2 = word.index(letter)
                    print()
                    print(letter)
                    print(myWord)
                    print(index1)
                    print(word)
                    print(index2)
                    updatePlainText(cipherText.index(myWord), cipherText.index(word), index1, index2, possiblePlainText)

def updatePlainText(myIndex, curIndex, index1, index2, possiblePlainText):
    list1 = []
    list2 = []

    for word1 in possiblePlainText[myIndex]:
        for word2 in possiblePlainText[curIndex]:
            if word1[index1] == word2[index2]:
                print(word1)
                print(word2)
                print()
                list1.append(word1)
                list2.append(word2)

    print(len(list2))

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
    for word in cipherText:
        checkWordsWithSameLetter(word, cipherText, possiblePlainText)
    for index in range(0,len(possiblePlainText)):
        if len(possiblePlainText[index]) == 1:
            keyUpdated = updateKey(key,possiblePlainText[index][0],cipherText[index])
    print(key)
    useKey(cipherText, key)
    complete = decoded(possiblePlainText)
    done = (not(keyUpdated) and not(complete)) or complete
print("done")
for words in possiblePlainText:
    print(len(words))
            
