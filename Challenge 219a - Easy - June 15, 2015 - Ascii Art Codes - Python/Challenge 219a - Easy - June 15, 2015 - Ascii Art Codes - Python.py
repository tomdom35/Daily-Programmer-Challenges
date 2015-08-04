import sys
from random import randint
def getAsciiCode(file):
    code = ''
    for line in file:
        for char in line:
            asciiValue = ord(char)
            if(asciiValue<10):
                code+='00'+str(asciiValue)
            elif(asciiValue<100):
                code+='0'+str(asciiValue)
            else:
                code+=str(asciiValue)
    return code

def makeAsciiArt(code):
    for i in range(0,int(len(code)/3)):
        index = 3*i
        sys.stdout.write(chr(int(code[index:index+3])))

def getNonSpaceCode(code):
    newCode = ''
    for i in range(0,int(len(code)/3)):
        index = 3*i
        if(code[index:index+3] != '032' and code[index:index+3] != '010'):
            newCode += code[index:index+3]
    return newCode

def getInvertCode(code, nonSpaceCode):
    index2 = 0
    newCode = ''
    for i in range(0,int(len(code)/3)):
        index = 3*i
        if(code[index:index+3] == '032'):
            if(index2>=len(nonSpaceCode)):
                index2 = 0
            newCode += nonSpaceCode[index2:index2+3]
            index2+=3
        elif(code[index:index+3] == '010'):
            newCode += '010'
        else:
            newCode += '032'
    return newCode


file = open('Ascii Art.txt')
code = getAsciiCode(file)
nonSpaceCode = getNonSpaceCode(code)
invertCode = getInvertCode(code,nonSpaceCode)
print (code)
print()
#print (nonSpaceCode)
#print()
#print(invertCode)
#print()

#print()
makeAsciiArt(code))
