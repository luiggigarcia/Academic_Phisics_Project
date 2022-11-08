from math import sqrt, pow

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

def VelocityXBall(timeList):
    vx = []
    for t in timeList:
        v = -0.021 * t**2 - 0.34*t + 2.5
        vx.append(v)
    return vx

def VelocityYBall(timeList):
    vy = []
    for t in timeList:
        v = -0.4*t + 1.8
        vy.append(v)
    return vy

def AccelerationXBall(timeList):
    ax = []
    for t in timeList:
        a = -0.042*t - 0.34
        ax.append(a)
    return ax

def AccelerationYBall(timeList):
    ay = []
    for t in timeList:
        a = -0.4
        ay.append(a)
    return ay

def PositionXRobot(timeList, xo, ball_posx):
    # Uma forma interessante de calcular também seria com a função da posição por tempo
    # S = S0 + V*t
    
    robot_posx = []
    file = open("./txt_files/robot_positionx.txt", 'w')
    
    for t in range(len(timeList)):
        if xo > ball_posx[t]:
            xo -= 0.50
        else:
            xo += 0.50
            
        robot_posx.append(xo)
            
        if (t == (len(timeList) - 1)):
            file.write("%f" % xo)
        else:
            file.write("%f\n" % xo)
        
    file.close()
    return robot_posx

def PositionYRobot(timeList, yo, ball_posx):
    robot_posy = []
    file = open("./txt_files/robot_positiony.txt", 'w')
    
    for t in range(len(timeList)):
        if yo > ball_posx[t]:
            yo -= 0.35
        else:
            yo += 0.35
            
        robot_posy.append(yo)
            
        if t == len(timeList) - 1:
            file.write("%f" % yo)
        else:
            file.write("%f\n" % yo)
        
    file.close()
    return robot_posy

def VelocityRobot(timeList, vo, a):
    #v(t) = vo + a*t
    v = []
    time = []
    
    for t in range(len(timeList)):
        vt = vo + (a*t)
        if vt >= 2.8:
            v.append(vt)
            time.append(timeList[t])
            break
        
        v.append(vt)
        time.append(timeList[t])
        
    return [v, time]

def AccelerationRobot(timeList, ac):
    a = []
    
    for t in range(len(timeList)):
        a.append(ac)
        
    return a