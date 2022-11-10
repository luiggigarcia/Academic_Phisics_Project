file = open("trajectory.txt", 'r')
data = file.readlines()
dataList = []
    
for line in data:
    line = line.replace(',', '.').strip().split()
    dataList.append(line)
    
file.close()

file_ballTime = open("ball_time.txt", 'w')
for i in range(len(dataList)):
    if i == len(dataList) - 1: # Condicional para a escrita da última linha.
        file_ballTime.write(dataList[i][0])
        break
    file_ballTime.write(dataList[i][0]+'\n')
        
file_ballTime.close()
    
file_ballPositionx = open("positions_x.txt", 'w')
for i in range(len(dataList)):
    if i == len(dataList) - 1:
        file_ballPositionx.write(dataList[i][1])
        break
    file_ballPositionx.write(dataList[i][1]+'\n')
        
file_ballPositionx.close()
    
file_ballPositiony = open("positions_y.txt", 'w')
for i in range(len(dataList)):
    if i == len(dataList) - 1:
        file_ballPositiony.write(dataList[i][2])
        break
    file_ballPositiony.write(dataList[i][2]+'\n')
        
file_ballPositiony.close()