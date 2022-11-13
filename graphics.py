from data import *
from main import afterList as interception

data = interception[0]
ball = interception[1]
robot = interception[2]

# As listas estão dentro de cada dicionário
# Exemplo -> ball["xList"], ball["timeList"], robot["vxList"], ...

# Todas as listas até o momento da interceptação
# print(ball["timeList"]) # Lista dos tempos da interceptação
# print(ball["xList"]) 
# print(ball["yList"]) 
# print(ball["vxList"]) 
# print(ball["vyList"]) 
# print(ball["axList"]) 
# print(ball["ayList"])

# print(robot["xList"]) 
# print(robot["yList"])
# print(robot["vxList"])
# print(robot["vyList"])
# print(robot["axList"])
# print(robot["ayList"])
# Para o grafico da distancia relativa em função do tempo
# print(data["distanceList"])