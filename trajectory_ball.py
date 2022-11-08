file = open("./txt_files/trajectory_ball.txt", 'r')
data = file.readlines()
dataList = []
    
for line in data:
    line = line.replace(',', '.').strip().split()
    dataList.append(line)
    
file.close()

file_ballTime = open('./txt_files/ball_time.txt', 'w')
for i in range(len(dataList)):
    if i == len(dataList) - 1:
        file_ballTime.write(dataList[i][0])
        break
    file_ballTime.write(dataList[i][0]+'\n')
        
file_ballTime.close()
    
file_ballPositionx = open('./txt_files/ball_positionx.txt', 'w')
for i in range(len(dataList)):
    if i == len(dataList) - 1:
        file_ballPositionx.write(dataList[i][1])
        break
    file_ballPositionx.write(dataList[i][1]+'\n')
        
file_ballPositionx.close()
    
file_ballPositiony = open('./txtfiles/ball_positiony.txt', 'w')
for i in range(len(dataList)):
    if i == len(dataList) - 1:
        file_ballPositiony.write(dataList[i][2])
        break
    file_ballPositiony.write(dataList[i][2]+'\n')
        
file_ballPositiony.close()