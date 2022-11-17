from data import *
from aprofundamento import afterList as interception
import matplotlib.pyplot as plt

data = interception[0]
ball = interception[1]
robot = interception[2]

# GRÁFICO 1
def trajetoria(xList_robot, yList_robot, xList_ball, yList_ball, str):  
  plt.plot(xList_ball, yList_ball, label= "Bola")
  plt.plot(xList_robot,yList_robot, label= "Robô")
  plt.legend()
  plt.title("%s" % str)
  plt.xlabel("Posição x(m)")
  plt.ylabel("Posição y(m)")
  plt.show()

xList_ball = [ball["xList"][0], ball["xList"][-1]]
yList_ball = [ball["yList"][0], ball["yList"][-1]]
xList_robot = [robot["xList"][0], robot["xList"][-1]]
yList_robot = [robot["yList"][0], robot["yList"][-1]]
trajetoria(xList_robot, yList_robot, xList_ball, yList_ball, "Trajetória da Bola e do Robô em xy")

# GRÁFICO 2

def x_posicao(t, xb, xr):  
  plt.plot(t,xb, label= "Bola")
  plt.plot(t,xr, label= "Robô")
  plt.legend()
  plt.title("Posição x da bola e do robô em função do tempo")
  plt.xlabel("Tempo(s)")
  plt.ylabel("Posição x(m)")
  plt.show()

time = ball["timeList"]
t = [time[0], time[-1]]
xr = [robot["xList"][0], robot["xList"][-1]]
xb = [ball["xList"][0], ball["xList"][-1]]

x_posicao(t, xb, xr)

def y_posicao(t, yb, yr):  
  plt.plot(t,yb, label= "Bola")
  plt.plot(t,yr, label= "Robô")
  plt.legend()
  plt.title("Posição y da bola e do robô em função do tempo")
  plt.xlabel("Tempo(s)")
  plt.ylabel("Posição y(m)")
  plt.show()

yb = [ball["yList"][0], ball["yList"][-1]]
yr = [robot["yList"][0], robot["yList"][-1]]

y_posicao(t, yb, yr)
# ==========================

# GRÁFICO 3
def x_velocidade(t, vx_ball, vx_robot):  
  plt.plot(t,vx_ball, label= "Bola")
  plt.plot(t,vx_robot, label= "Robô")
  plt.legend()
  plt.title("Velocidade em x da bola e do robô em função do tempo")
  plt.xlabel("Tempo(s)")
  plt.ylabel("Velocidade x(m/s)")
  plt.show()

vb = ball["vxList"]
vx_ball = [vb[0],vb[-1]]
vr = robot["vxList"]
vx_robot = [vr[0], vr[-1]]

x_velocidade(t, vx_ball, vx_robot)

def y_velocidade(t, vy_ball, vy_robot): 
  plt.plot(t,vy_ball, label= "Bola")
  plt.plot(t,vy_robot, label= "Robô")
  plt.legend()
  plt.title("Velocidade em y da bola e do robô em função do tempo")
  plt.xlabel("Tempo(s)")
  plt.ylabel("Velocidade y(m/s)")
  plt.show()

vb = ball["vyList"]
vy_ball = [vb[0], vb[-1]]
vr = robot["vyList"] 
vy_robot = [vr[0], vr[-1]]

y_velocidade(t, vy_ball, vy_robot)
# =============================================

# GRÁFICO 4
def x_aceleracao(t, ax_ball, ax_robot):  
  plt.plot(t,ax_ball, label= "Bola")
  plt.plot(t,ax_robot, label= "Robô")
  plt.legend()
  plt.title("Aceleração em x da bola e do robô em função do tempo")
  plt.xlabel("Tempo(s)")
  plt.ylabel("Aceleração x(m/s²)")
  plt.show()

ab = ball["axList"]
ax_ball = [ab[0], ab[-1]]
ar = robot["axList"]
ax_robot = [ar[0], ar[-1]]

x_aceleracao(t, ax_ball, ax_robot)

def y_aceleracao(t, ay_ball, ay_robot):  
  plt.plot(t,ay_ball, label= "Bola")
  plt.plot(t,ay_robot, label= "Robô")
  plt.legend()
  plt.title("Aceleração em y da bola e do robô em função do tempo")
  plt.xlabel("Tempo(s)")
  plt.ylabel("Aceleração y(m/s²)")
  plt.show()

ab = ball["ayList"]
ay_ball = [ab[0], ab[-1]]
ar = robot["ayList"]
ay_robot = [ar[0], ar[-1]]

y_aceleracao(t, ay_ball, ay_robot)

# ========================

# GRÁFICO 5
def distanciaRelativa(xList_ball, yList_ball, xList_robot, yList_robot):
  plt.plot(xList_ball,yList_ball, label= "Bola")
  plt.plot(xList_robot,yList_robot, label= "Robô")
  plt.legend()
  plt.title("Distância relativa entre o robô e a bola em função do tempo")
  plt.xlabel("Posição x(m)")
  plt.ylabel("Posição y(m)")
  plt.show()

distanciaRelativa(xList_ball, yList_ball, xList_robot, yList_robot)

# APROFUNDAMENTO - RAIO DE INTERCEPTAÇÃO DIMINUIDO

# ------------- Com Raio em 0.9m ----------------
data2 = interception[3]
xList_ball = [data2["ballxList"][0], data2["ballxList"][-1]]
yList_ball = [data2["ballyList"][0], data2["ballyList"][-1]]
xList_robot = [data2["robotxList"][0], data2["robotxList"][-1]]
yList_robot = [data2["robotyList"][0], data2["robotyList"][-1]]
trajetoria(xList_robot, yList_robot, xList_ball, yList_ball, "Trajetória da Bola e do Robô em xy com raio diminuido em 0.9m")