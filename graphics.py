from data import *
from interface import afterList as interception
import matplotlib.pyplot as plt

data = interception[0]
ball = interception[1]
robot = interception[2]

# GRÁFICO 1
def trajetoria():  
  xb = ball["xList"]
  xList_ball = [xb[0], xb[-1]]
  yb = ball["yList"]
  yList_ball = [yb[0], yb[-1]]
  xr = robot["xList"]
  xList_robot = [xr[0], xr[-1]]
  yr = robot["yList"]
  yList_robot = [yr[0], yr[-1]]
  plt.plot(xList_ball, yList_ball, label= "Bola")
  plt.plot(xList_robot,yList_robot, label= "Robô")
  plt.legend()
  plt.title("Trajetória da Bola e do Robô em xy")
  plt.xlabel("Posição x(m)")
  plt.ylabel("Posição y(m)")
  plt.show()

trajetoria()

# GRÁFICO 2

time = ball["timeList"]
t = [time[0], time[-1]]

def x_posicao():  
  x = robot["xList"]
  xr = [x[0],x[-1]]
  xb = ball["xList"]
  x_b = [xb[0],xb[-1]]
  plt.plot(t,x_b, label= "Bola")
  plt.plot(t,xr, label= "Robô")
  plt.legend()
  plt.title("Posição x da bola e do robô em função do tempo")
  plt.xlabel("Tempo(s)")
  plt.ylabel("Posição x(m)")
  plt.show()

x_posicao()

def y_posicao():  
  yb = ball["yList"]
  y_b = [yb[0], yb[-1]]
  y = robot["yList"]
  yr = [y[0], y[-1]]
  plt.plot(t,y_b, label= "Bola")
  plt.plot(t,yr, label= "Robô")
  plt.legend()
  plt.title("Posição y da bola e do robô em função do tempo")
  plt.xlabel("Tempo(s)")
  plt.ylabel("Posição y(m)")
  plt.show()

y_posicao()
# ==========================

# GRÁFICO 3
def x_velocidade():  
  v = ball["vxList"]
  vx_ball = [v[0],v[-1]]
  vr = robot["vxList"]
  vx_robot = [vr[0], vr[-1]]
  robot["vxList"]
  plt.plot(t,vx_ball, label= "Bola")
  plt.plot(t,vx_robot, label= "Robô")
  plt.legend()
  plt.title("Velocidade em x da bola e do robô em função do tempo")
  plt.xlabel("Tempo(s)")
  plt.ylabel("Velocidade x(m/s)")
  plt.show()

x_velocidade()

def y_velocidade(): 
  v = ball["vyList"]
  vy_ball = [v[0], v[-1]]
  vr = robot["vyList"] 
  vy_robot = [vr[0], vr[-1]]
  plt.plot(t,vy_ball, label= "Bola")
  plt.plot(t,vy_robot, label= "Robô")
  plt.legend()
  plt.title("Velocidade y da bola e do robô em função do tempo")
  plt.xlabel("Tempo(s)")
  plt.ylabel("Velocidade y(m/s)")
  plt.show()

y_velocidade()
# =============================================

# GRÁFICO 4
def x_aceleracao():  
  a = ball["axList"]
  ax_ball = [a[0], a[-1]]
  ar = robot["axList"]
  ax_robot = [ar[0], ar[-1]]
  plt.plot(t,ax_ball, label= "Bola")
  plt.plot(t,ax_robot, label= "Robô")
  plt.legend()
  plt.title("Aceleração em x da bola e do robô em função do tempo")
  plt.xlabel("Tempo(s)")
  plt.ylabel("Aceleração x(m/s²)")
  plt.show()

x_aceleracao()

def y_aceleracao():  
  a = ball["ayList"]
  ay_ball = [a[0], a[-1]]
  ar = robot["ayList"]
  ay_robot = [ar[0], ar[-1]]
  plt.plot(t,ay_ball, label= "Bola")
  plt.plot(t,ay_robot, label= "Robô")
  plt.legend()
  plt.title("Aceleração em y da bola e do robô em função do tempo")
  plt.xlabel("Tempo(s)")
  plt.ylabel("Aceleração y(m/s²)")
  plt.show()

y_aceleracao()

# ========================

# GRÁFICO 5
def distanciaRelativa():  
  xb = ball["xList"]
  xList_ball = [xb[0], xb[-1]]
  yb = ball["yList"]
  yList_ball = [yb[0], yb[-1]]
  xr = robot["xList"]
  xList_robot = [xr[0], xr[-1]]
  yr = robot["yList"]
  yList_robot = [yr[0], yr[-1]]
  plt.plot(xList_ball,yList_ball, label= "Bola")
  plt.plot(xList_robot,yList_robot, label= "Robô")
  plt.legend()
  plt.title("Distância relativa entre robô e bola")
  plt.xlabel("Posição x(m)")
  plt.ylabel("Posição y(m)")
  plt.show()

distanciaRelativa()

# distancia_relativa()