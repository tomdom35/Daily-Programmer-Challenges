from ast import literal_eval
import math

def getSchedule(lines):
    schedule = []
    lines = lines[1:]
    for line in lines:
        l = line.split()
        units = int(l[0])
        location = literal_eval(l[1])
        order = (units,location)
        schedule.append(order)
    return schedule

def distance(location1, location2):
    x1 = location1[0]
    x2 = location2[0]
    y1 = location1[1]
    y2 = location2[1]
    return math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))

def getClosestDelivery(location, deliverySchedule, truckLoad):
    shortestDistance = 100000000
    nextDelivery = (-1,(-1,-1))
    for delivery in deliverySchedule:
        newLocation = delivery[1]
        if(newLocation != location and delivery[0] <= truckLoad):
            dist = distance(location, newLocation)
            if(dist < shortestDistance):
                shortestDistance = dist
                nextDelivery = delivery
    return nextDelivery

def canDeliver(truckLoad,deliverySchedule):
    for delivery in deliverySchedule:
        if(delivery[0] <= truckLoad):
            return True
    return False

file = open('input.txt')
firstLine = file.readline().split()
truckCapacity = int(firstLine[0])
truckLoad = truckCapacity
depotLocation = literal_eval(firstLine[1])
truckLocation = depotLocation
lines = list(file)
deliverySchedule = getSchedule(lines)
routOrder = []
totalDistance = 0

print('Always go to closest delivery')

while(len(deliverySchedule) > 0):
    if(canDeliver(truckLoad,deliverySchedule)):
        nextDelivery = getClosestDelivery(truckLocation, deliverySchedule, truckLoad)
        if(nextDelivery[0]>0):
            routOrder.append(nextDelivery[1])
            totalDistance += distance(truckLocation,nextDelivery[1])
            truckLocation = nextDelivery[1]
            truckLoad -=nextDelivery[0]
            deliverySchedule.remove(nextDelivery)
    else:
        totalDistance += distance(truckLocation,depotLocation)
        routOrder.append(depotLocation)
        truckLoad = 40
        truckLocation = depotLocation

print(routOrder)
print(totalDistance, 'units')
