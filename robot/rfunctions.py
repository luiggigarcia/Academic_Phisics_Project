import sys
sys.path.insert(0, "../")
from functions import angle
from math import sin, cos

def vel(vo, a, t):
    v = vo + (a*t)
    return v

def Pos_Robot(timeList, ballList, xo, a, pos):
    file = open("./robot/positions_%s.txt" % pos, 'w')
    coordinates = [xo]
    x = xo
    file.write("%.3f\n" % x)
    
    for t in range(len(timeList)):
        v = vel(0, a, timeList[t])
        if (x < ballList[t]):
            x += (v*0.02)
        else:
            x -= (v*0.02)
            
        if t == len(timeList) - 1:
            file.write("%.3f" % x)
            break
        file.write("%.3f\n" % x)
            
        coordinates.append(x)
    
    file.close()
    return coordinates

def Ax_Robot(timeList):
    ax = []
    
    for t in timeList:
        ax.append(2.4)
        
    return ax

def Ay_Robot(timeList):
    ay = []
    
    for t in timeList:
        ay.append(2.4)
        
    return ay

def Vx_Robot(timeList, Bx, By, Rx, Ry, v):
    vx = []
    for t in range(len(timeList)):
        ang = angle(Bx[t], By[t], Rx[t], Ry[t])
        vel = cos(ang) * v
        # print("%.2f m/s" % vel)
        vx.append(round(vel, 3))
    return vx
        

def Vy_Robot(timeList, Bx, By, Rx, Ry, v):
    vy = []
    for t in range(len(timeList)):
        ang = angle(Bx[t], By[t], Rx[t], Ry[t])
        vel = sin(ang) * v
        vy.append(round(vel, 3))
    return vy
