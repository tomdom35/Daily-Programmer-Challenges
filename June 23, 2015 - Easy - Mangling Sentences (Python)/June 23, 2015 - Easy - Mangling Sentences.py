def order(word):
    uppercaseIndices = []
    punctuationIndices = []
    punctuationMarks = []
    for char in word:
        if char.isupper():
            uppercaseIndices.append(word.index(char))
        elif(not(char.isalpha())):
            punctuationIndices.append(word.index(char))
            punctuationMarks.append(char)
    word = word.lower()
    wordList = list(sorted(word))
    wordList = setPunctuation(wordList, punctuationIndices, punctuationMarks)
    wordList = setUppercase(wordList, uppercaseIndices)
    wordList.append(" ")
    return "".join(wordList)

def setPunctuation(wordList, punctuationIndices, punctuationMarks):
    for index in range(0,len(wordList)):
        if index in punctuationIndices:
            markIndex = punctuationIndices.index(index)
            wordList.insert(index+1,punctuationMarks[markIndex])
            wordList.remove(punctuationMarks[markIndex])
    return wordList

def setUppercase(wordList, uppercaseIndices):
    for index in range(0,len(wordList)):
        if index in uppercaseIndices:
            wordList[index] = wordList[index].upper()
    return wordList

def makeOrderedSentence(words):
    orderedWords = []
    for word in words:
        orderedWords.append(order(word))
    return "".join(orderedWords)

def getOrderedSentence(sentence):
    words = sentence.split()
    orderedSentence = makeOrderedSentence(words)
    print(sentence)
    print(orderedSentence)
    print()

sentence1 = "Eye of Newt, and Toe of Frog, Wool of Bat, and Tongue of Dog."
sentence2 = "Adder's fork, and Blind-worm's sting, Lizard's leg, and Howlet's wing."
sentence3 = "For a charm of powerful trouble, like a hell-broth boil and bubble."
getOrderedSentence(sentence1)
getOrderedSentence(sentence2)
getOrderedSentence(sentence3)

