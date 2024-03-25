import math
def solution(n, stations, w):
    answer = 0
    result = w * 2 + 1 # 3
    start = 1
    end = 1
    for station in stations:
        end = station-w
        answer += math.ceil((end-start)/result)
        start = station+w+1
        
        
    # 뒷 자리가 끝이 아닐때
    if end < start:
        end = n+1
        answer += math.ceil((end-start)/result)
        
    return answer