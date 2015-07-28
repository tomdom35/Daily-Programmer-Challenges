def findPermutations(letters):
    permutations = []
    if(len(letters) == 2):
        permutations.append(''.join(letters))
        permutations.append(''.join(list(reversed(letters))))
        return permutations
    for i in range(0,len(letters)):
        newLetters = letters[:i]+letters[i+1:]
        tempPerms = findPermutations(newLetters)
        for perm in tempPerms:
             permutation = (letters[i] + perm)
             permutations.append(permutation)
    return permutations

def makeLangfordStrings(permutations,letterList):
    langfordStrings = []
    for permutation in permutations:
        newString = creatEmptyString(len(letterList))
        langford = True
        for letter in permutation:
            spaceIndex = newString.index(' ')
            newString[spaceIndex] = letter
            letterDist = letterList.find(letter)+1
            newIndex = spaceIndex + letterDist + 1
            if(newIndex < len(newString) and newString[newIndex] == ' '):
                newString[newIndex] = letter
            else:
                langford = False
                break
        if(langford):
            langfordStrings.append(''.join(newString))
    return langfordStrings

def creatEmptyString(length):
    emptyString = []
    for i in range(0,length*2):
        emptyString.append(' ')
    return emptyString

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = 4
letterList = alpha[0:N]
permutations = findPermutations(list(letterList))
langfordStrings = makeLangfordStrings(permutations,letterList)
for string in langfordStrings:
    print(string)



    
