from data import beforeIntercept, afterIntercept
robot_xo = float(input("Digite a coordenada xo do robo: "))
robot_yo = float(input("Digite a coordenada yo do robo: "))
vo_robot = 0.84 # 30% de da velocidade.
a_robot = 2.4
vmax = 2.4
raio = 0.11

beforeList = beforeIntercept(robot_xo, robot_yo, vmax)
afterList = afterIntercept(beforeList[0], beforeList[1], raio)
data_interception = afterList[0]


print(f"Interception: {data_interception['interception']}")
print("Distance Robot and Ball: %.3f(m)" % data_interception["distance"])
print("Interception Time: %.2f(s)" % data_interception["time"])
print("Coordenadas da interceptação:")
print("Robotx: %.2f, Roboty: %.2f" % (data_interception["robotX"], data_interception["robotY"]))
print("Ballx: %.2f, Bally: %.2f" % (data_interception["ballX"], data_interception["ballY"]))

# distancia < raioRobo + raioBola
# Então interceptação