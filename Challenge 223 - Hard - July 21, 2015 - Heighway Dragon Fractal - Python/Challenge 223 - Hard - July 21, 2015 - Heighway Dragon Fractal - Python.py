def findFractal(n):
    directions = []
    for i in range(0,n+1):
        if i == 0:
            directions.append(4)
        else:
            newDirections = shiftRight(directions)
            newDirections = list(reversed(newDirections))
            directions += newDirections
    return directions

def shiftRight(directions):
    newDirections = []
    for i in range(0,len(directions)):
        if(directions[i]==4):
            newDirections.append(1)
        else:
            newDirections.append(directions[i] + 1)
    return newDirections

def findPointsAndSumOptomized(n):
    directions = findFractal(n)
    point = (0,0)
    xSum = 0
    ySum = 0
    #Showing all the points for anything over n = 12 is just overkill
    if n <=12 : print(point)
    for i in directions:
        if(i==1):
            point = (point[0],point[1] + 1)
        elif(i==2):
            point = (point[0] - 1, point[1])
        elif(i==3):
            point = (point[0],point[1] - 1)
        else:
            point = (point[0] + 1, point[1])
        if n <=12 : print(point)
        xSum += point[0]
        ySum += point[1]
    print('Sum of X\'s =',xSum)
    print('Sum of Y\'s =',ySum)
    
findPointsAndSumOptomized(16)
