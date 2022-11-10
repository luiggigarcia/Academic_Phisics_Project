from math import sqrt, pow, atan2

def distance(robotx, roboty, ballx, bally):
    dist = sqrt(pow(robotx - ballx, 2) + pow(roboty - bally, 2))
    return dist

def interception(timeList, robotxList, robotyList, ballxList, ballyList, raio):
    dist, timeIntercept, collision = 0, 0, False
    robotxIntercept, robotyIntercept, ballxIntercept, ballyIntercept = 0, 0, 0, 0
    robotxListIntercept, robotyListIntercept = [], []
    ballxListIntercept, ballyListIntercept = [], []
    timeListIntercept = []
    
    for t in range(len(timeList)):
        dist = distance(robotxList[t], robotyList[t], ballxList[t], ballyList[t])
        timeListIntercept.append(timeList[t])
        robotxListIntercept.append(robotxList[t])
        robotyListIntercept.append(robotyList[t])
        ballxListIntercept.append(ballxList[t])
        ballyListIntercept.append(ballyList[t])
        
        if dist < raio:
            collision = True
            timeIntercept = timeList[t]
            robotxIntercept = robotxList[t]
            robotyIntercept = robotyList[t]
            ballxIntercept = ballxList[t]
            ballyIntercept = ballyList[t]
            break
        
    return [
        [collision, dist, timeIntercept, robotxIntercept, robotyIntercept, 
         ballxIntercept, ballyIntercept],
        [timeListIntercept, robotxListIntercept, robotyListIntercept,
         ballxListIntercept, ballyListIntercept]]
    
def readFileToList(filename):
    file = open(filename, 'r')
    data = file.readlines()
    dataList = []
    
    for i in data:
        i = float(i.strip())
        dataList.append(i)
        
    return dataList

def angle(dy, dx):
    ang = atan2(dy, dx)
    return ang