from ball.bfunctions import *
from robot.rfunctions import *
from functions import *


# # Dados fornecidos antes da interceptação

def beforeIntercept(robot_xo, robot_yo, vmax):
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
        "xList": Posx_Robot(ball["timeList"], ball["xList"][0], ball["yList"][0], robot_xo, robot_yo, vmax),
        "yList": Posy_Robot(ball["timeList"], ball["xList"][0], ball["yList"][0], robot_xo, robot_yo, vmax),
    }
    
    dy = ball["yList"][0] - robot_yo
    dx = ball["xList"][0] - robot_xo
    ang = angle(dy, dx)
    
    robot["vxList"] = Vx_Robot(ball["timeList"], ang, vmax)
    robot["vyList"] = Vy_Robot(ball["timeList"], ang, vmax)
    
    return [ball, robot]



# # Dados fornecidos após a interceptação da bola

def afterIntercept(ball, robot, raio):
    
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

    robotIntercept = {
        "xList": M_intercept[1][1],
        "yList": M_intercept[1][2]
    }
    
    return [data_interception, ballIntercept, robotIntercept]