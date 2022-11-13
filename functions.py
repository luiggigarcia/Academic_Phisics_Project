from math import sqrt, pow, atan

def distance(robotx, roboty, ballx, bally):
    dist = sqrt(pow(ballx - robotx, 2) + pow(bally - roboty, 2))
    return dist

def distanceList(timeList, Rx, Ry, Bx, By):
    distances = []
    for t in range(len(timeList)):
        aux1 = (Bx[t] - Rx[t])**2
        aux2 = (By[t] - Ry[t])**2
        d = sqrt(aux1 + aux2)
        distances.append(round(d, 3))
    return distances

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
        # print("Distance: %.2f < 0.11" % dist)
        
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


def angle(Bx, By, Rx, Ry):
    if By - Ry == 0:
        return 0
    aux = (Bx - Rx) / (By - Ry)
    aux = aux**2
    mod_tangent = sqrt(aux)
    ang = atan(mod_tangent)
    return ang

def TrajectoryTime(dist, v):
    t = dist/v
    print("Tempo da trajetória: %.2f" % t)
    return t