def Vx_Ball(timeList):
    vx = []
    for t in timeList:
        v = (-0.021 * t**2) -0.34*t + 2.5
        vx.append(round(v, 3))
    return vx

def Vy_Ball(timeList):
    vy = []
    for t in timeList:
        v = -0.4*t + 1.8
        vy.append(round(v, 3))
    return vy

def Ax_Ball(timeList):
    ax = []
    for t in timeList:
        a = -0.042*t - 0.34
        ax.append(round(a, 3))
    return ax

def Ay_Ball(timeList):
    ay = []
    for t in timeList:
        a = -0.4
        ay.append(round(a, 3))
    return ay