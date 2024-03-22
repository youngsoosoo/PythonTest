def solution(lines):
    answer = 0
    logs = []
    
    for line in lines:
        date, endTime, time = line.split()
        endTime = endTime.split(":")
        time = time.replace('s', '')
        
        
        endTime = (int(endTime[0])*3600 + int(endTime[1])*60 + float(endTime[2])) * 1000
        startTime = endTime - float(time) * 1000 + 1
        logs.append([startTime, endTime])
    
    for i in range(len(logs)):
        cnt = 0
        for j in range(i, len(logs)):
            if logs[i][1] + 1000 > logs[j][0]:
                cnt += 1
        
        answer = max(answer, cnt)
    
    return answer