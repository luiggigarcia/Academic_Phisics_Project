from data import beforeIntercept, afterIntercept
from functions import *
robot_xo = float(input("Digite a coordenada xo do robo: "))
robot_yo = float(input("Digite a coordenada yo do robo: "))
a = 2.4
v = 2.8
raio = 0.11

beforeList = beforeIntercept(robot_xo, robot_yo, a, v)
afterList = afterIntercept(beforeList[0], beforeList[1], raio, v)
data_interception = afterList[0]
distCm = data_interception["distance"] * 100

print(f"Interception: {data_interception['interception']}")
print("Distance Robot->Ball: %.3f(m) | %.2fcm" % (data_interception["distance"], distCm))
print("Interception Time: %.2f(s)" % data_interception["time"])
print("Coordenadas da interceptação:")
print("Robotx: %.2f, Roboty: %.2f" % (data_interception["robotX"], data_interception["robotY"]))
print("Ballx: %.2f, Bally: %.2f" % (data_interception["ballX"], data_interception["ballY"]))