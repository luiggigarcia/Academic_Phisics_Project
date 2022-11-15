from ball.bfunctions import *
from robot.rfunctions import *
from functions import *


# # Dados fornecidos antes da interceptação

def beforeIntercept(robot_xo, robot_yo, a, v):
    ball = {
        "timeList": readFileToList('./ball/ball_time.txt'),
        "xList": readFileToList('./ball/positions_x.txt'),
        "yList": readFileToList('./ball/positions_y.txt')
    }

    ball["vxList"] = Vx_Ball(ball["timeList"])
    ball["vyList"] = Vy_Ball(ball["timeList"])
    ball["axList"] = Ax_Ball(ball["timeList"])
    ball["ayList"] = Ay_Ball(ball["timeList"])

    robot = {
        "xList": Pos_Robot(ball["timeList"], ball["xList"], robot_xo, a, "x"),
        "yList": Pos_Robot(ball["timeList"], ball["yList"], robot_yo, a, "y")
    }
    
    
    robot["vxList"] = Vx_Robot(ball["timeList"], ball["xList"], ball["yList"], robot["xList"], robot["yList"], v) 
    robot["vyList"] = Vy_Robot(ball["timeList"], ball["xList"], ball["yList"], robot["xList"], robot["yList"], v)
    
    return [ball, robot]



# # Dados fornecidos após a interceptação da bola

def afterIntercept(ball, robot, raio, v):
    
    M_intercept = interception(ball["timeList"], robot["xList"], robot["yList"], ball["xList"], ball["yList"], raio)
    
    data_interception = {
        "interception": M_intercept[0][0],
        "distance": M_intercept[0][1],
        "time": M_intercept[0][2],
        "robotX": M_intercept[0][3],
        "robotY": M_intercept[0][4],
        "ballX": M_intercept[0][5],
        "ballY": M_intercept[0][6],
        "distanceList": distanceList(M_intercept[1][0], M_intercept[1][1], M_intercept[1][2], M_intercept[1][3], M_intercept[1][4])
    }

    ballIntercept = {
        "timeList": M_intercept[1][0],
        "xList": M_intercept[1][3],
        "yList": M_intercept[1][4],
        "vxList": Vx_Ball(ball["timeList"]),
        "vyList": Vy_Ball(ball["timeList"]),
        "axList": Ax_Ball(ball["timeList"]),
        "ayList": Ay_Ball(ball["timeList"])
    }

    robotIntercept = {
        "xList": M_intercept[1][1],
        "yList": M_intercept[1][2],
        "vxList": Vx_Robot(ball["timeList"], ball["xList"], ball["yList"], robot["xList"], robot["yList"], v),
        "vyList": Vy_Robot(ball["timeList"], ball["xList"], ball["yList"], robot["xList"], robot["yList"], v),
        "axList": Ax_Robot(ball["timeList"]),
        "ayList": Ay_Robot(ball["timeList"])
    }
    
    data_interception["robotDislocation"] = dislocation(robotIntercept["xList"][-1], robotIntercept["xList"][0])
    data_interception["robotVm"] = Vm(robotIntercept["xList"][-1], robotIntercept["xList"][0], ballIntercept["timeList"][-1], ballIntercept["timeList"][0])
    data_interception["robotAm"] = Am(robotIntercept["vxList"][-1], robotIntercept["vxList"][0], ballIntercept["timeList"][-1], ballIntercept["timeList"][0])
    data_interception["distTraveled"] = distanceTraveled(ballIntercept["timeList"], 0.4)
    return [data_interception, ballIntercept, robotIntercept]