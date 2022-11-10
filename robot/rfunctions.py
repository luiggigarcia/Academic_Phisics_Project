import sys
sys.path.insert(0, "../")
from functions import angle
from math import sin, cos

def Vx_Robot(timeList, angle, vmax):
    vx = []
    
    for t in range(len(timeList)):
        v = cos(angle) * vmax
        vx.append(v)
    
    return vx

def Vy_Robot(timeList, angle, vmax):
    vy = []
    
    for t in range(len(timeList)):
        v = sin(angle) * vmax
        vy.append(v)
        
    return vy


def Posx_Robot(timeList, Bxo, Byo, Rxo, Ryo, vmax):
    file = open("./robot/positions_x.txt", 'w')
    dy = Byo - Ryo
    dx = Bxo - Rxo
    ang = angle(dy, dx)
    vx = Vx_Robot(timeList, ang, vmax)
    Rx = Rxo
    
    coordinates_x = []
    
    for t in range(len(timeList)):
        Rx += vx[t]
        coordinates_x.append(Rx)
        
        if t == len(timeList) - 1:
            file.write("%.3f" % Rx)
            break
        file.write("%.3f\n" % Rx)
        
    file.close()
    
    return coordinates_x

def Posy_Robot(timeList, Bxo, Byo, Rxo, Ryo, vmax):
    file = open("./robot/positions_y.txt", 'w')
    dy = Byo - Ryo
    dx = Bxo - Rxo
    ang = angle(dy, dx)
    vy = Vy_Robot(timeList, ang, vmax)
    Ry = Ryo
    
    coordinates_y = []
    
    for t in range(len(timeList)):
        Ry += vy[t]
        coordinates_y.append(Ry)
        
        if t == len(timeList) - 1:
            file.write("%.3f" % Ry)
            break
        file.write("%.3f\n" % Ry)
        
    file.close()
    
    return coordinates_y

def Ax_Robot():
    return 0

def Ay_Robot():
    return 0