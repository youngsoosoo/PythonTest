def solution(n, t, m, timetable):
    answer = ''
    
    crew = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    crew.sort()
    
    bus = [9*60 + t*i for i in range(n)]
    
    i = 0
    for b in bus:
        cnt = 0
        while cnt < m and i < len(crew) and crew[i] <= b:
            i+=1
            cnt+=1
        
        if cnt < m:
            answer = b
        else:
            answer = crew[i-1]-1
    
    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)