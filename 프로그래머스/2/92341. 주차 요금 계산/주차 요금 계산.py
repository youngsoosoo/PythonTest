import math
def solution(fees, records):
    answer = []
    
    dic = dict()
    
    for record in records:
        time, carNum, record  = record.split()
        time = list(map(int, time.split(':')))
        time = time[0] * 60 + time[1]
        
        if carNum in dic:
            # 차가 나갔다가 다시 들어온 경우
            if record == "IN":
                dic[carNum] = dic[carNum] - time
            # 차가 나가는 경우
            else:
                dic[carNum] = time + dic[carNum]
        else:
            dic[carNum] = -1 * time
        
    for key, value in sorted(dic.items()):
        if value <= 0:
            value += 1439
        sumValue = fees[1]
        if value == 0:
            sumValue = 0
        elif value > fees[0]:
            sumValue += (math.ceil((value-fees[0]) / fees[2]) * fees[3])
        answer.append(sumValue)
        
    return answer