from functions import *

robot_xo = float(input("Digite a coordenada xo do robo: "))
robot_yo = float(input("Digite a coordenada yo do robo: "))
vo_robot = 0.84 # 30% de da velocidade.
ace_robot = 2.8
taxaAceRobot = 0.14 # aceleração média do robo.
raio = 0.11


# Dados fornecidos antes da interceptação

def beforeIntercept():
    ball = {
        "timeList": readFileToList('./txt_files/ball_time.txt'),
        "xList": readFileToList('./txt_files/ball_positionx.txt'),
        "yList": readFileToList('./txt_files/ball_positiony.txt')
    }

    ball["vxList"] = VelocityXBall(ball["timeList"])
    ball["vyList"] = VelocityYBall(ball["timeList"])
    ball["axList"] = AccelerationXBall(ball["timeList"])
    ball["ayList"] = AccelerationYBall(ball["timeList"])

    robot = {
        "xList": PositionXRobot(ball["timeList"], robot_xo, ball["xList"]),
        "yList": PositionYRobot(ball["timeList"], robot_xo, ball["yList"]),
        "vList": VelocityRobot(ball["timeList"], vo_robot, taxaAceRobot),
        "aList": AccelerationRobot(ball["timeList"], ace_robot)
    }
    
    return [ball, robot]



# Dados fornecidos após a interceptação da bola

def afterIntercept():
    data = beforeIntercept()
    ball = data[0]
    robot = data[1]
    
    M_intercept = interception(ball["timeList"], robot["xList"], robot["yList"], ball["xList"], ball["yList"], raio)
    
    data_interception = {
        "interception": M_intercept[0][0],
        "distance": M_intercept[0][1],
        "time": M_intercept[0][2],
        "robotX": M_intercept[0][3],
        "robotY": M_intercept[0][4],
        "ballX": M_intercept[0][5],
        "ballY": M_intercept[0][6]
    }

    ballIntercept = {
        "timeList": M_intercept[1][0],
        "xList": M_intercept[1][3],
        "yList": M_intercept[1][4]
    }

    ballIntercept["vxList"] = VelocityXBall(ballIntercept["timeList"])
    ballIntercept["vyList"] = VelocityYBall(ballIntercept["timeList"])
    ballIntercept["axList"] = AccelerationXBall(ballIntercept["timeList"])
    ballIntercept["ayList"] = AccelerationYBall(ballIntercept["timeList"])

    robotIntercept = {
        "xList": M_intercept[1][1],
        "yList": M_intercept[1][2],
        "v": VelocityRobot(ballIntercept["timeList"], vo_robot, taxaAceRobot),
        "a": AccelerationRobot(ballIntercept["timeList"])
    }
    
    return [data_interception, ballIntercept, robotIntercept]