def getLetter(n):
    if(n > 0 and n < 27):
        return chr(64+n)
    else:
        return ''

def getAlpha(n):
    done = False
    num = list(str(n))
    while( not done):
        if '0' in num:
            i = num.index('0')
            num[i]=getLetter(int(num[i-1]+num[i]))
            num[i-1]=''
        else:
            done = True
    partition(''.join(num),'',0)

def partition(num,s,index):
    string = s
    for i in range(index,len(num)):
        if(num[i].isalpha()):
            string+=num[i]
        elif(i<len(num)-1):
            if(num[i] == '1'):
                if(not num[i+1].isalpha()):
                    partition(num,string+getLetter(int(num[i]+num[i+1])),i+2)
                string+=getLetter(int(num[i]))
            elif(num[i] == '2'):
                if((not num[i+1].isalpha()) and int(num[i+1])<6):
                    partition(num,string+getLetter(int(num[i]+num[i+1])),i+2)
                string+=getLetter(int(num[i]))
            else:
                string+=getLetter(int(num[i]))
        else:
            string+=getLetter(int(num[i]))
    print(string)

getAlpha(12161212625815129412653221)
    

        
        
    
