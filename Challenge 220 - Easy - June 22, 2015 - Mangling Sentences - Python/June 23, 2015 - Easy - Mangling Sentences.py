def order(word):
    uppercaseIndices = []
    punctuationIndices = []
    punctuationMarks = []
    for index in range(0,len(word)):
        if word[index].isupper():
            uppercaseIndices.append(index)
        elif(not(word[index].isalpha())):
            punctuationIndices.append(index)
            punctuationMarks.append(word[index])
    word = word.lower()
    word = list(word)
    wordList = sorted(word)
    checkPunctuation(wordList, punctuationIndices, punctuationMarks)
    wordList = setUppercase(wordList, uppercaseIndices)
    wordList.append(" ")
    return "".join(wordList)

def checkPunctuation(wordList, punctuationIndices, punctuationMarks):
    for index in range(0,len(punctuationIndices)):
        markIndex = punctuationIndices[index]
        if wordList[markIndex] != punctuationMarks[index]:
            wordList = setPunctuation(wordList, punctuationIndices, punctuationMarks)
            checkPunctuation(wordList, punctuationIndices, punctuationMarks)

def setPunctuation(wordList, punctuationIndices, punctuationMarks):
    for index in range(0,len(wordList)):
        if index in punctuationIndices:
            markIndex = punctuationIndices.index(index)
            mark = punctuationMarks[markIndex]
            if wordList[index] != mark:
                wordList.insert(index+1,mark)
                wordList.remove(mark)
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
sentence4 = "George R.R. Martin doesn't like me"
getOrderedSentence(sentence1)
getOrderedSentence(sentence2)
getOrderedSentence(sentence3)
getOrderedSentence(sentence4)

