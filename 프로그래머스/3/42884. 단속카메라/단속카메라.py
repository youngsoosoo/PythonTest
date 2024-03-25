def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    result = -30001
    
    for route in routes:
        if route[0] > result:
            answer+=1
            result = route[1]
        
    return answer