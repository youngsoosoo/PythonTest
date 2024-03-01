def solution(cap, n, deliveries, pickups):
    answer = 0
    # delivery, pickup
    start = [0, 0]
    
    # 물류 창고에서 출발할 때 cap 만큼 가지고 나간다.
    # 물류 창고에서 돌아올 때 pickup의 크기는 cap으로 정한다.
    # 물류 창고로부터 제일 먼 곳 부터 배달을 실시하고, 알고리즘적으로 돌아올 때 남은 배달과 수거를 완료한다.
    for i in range(n-1, -1, -1):
        start[0] += deliveries[i]
        start[1] += pickups[i]
        
        while start[0] > 0 or start[1] > 0 :
            start[0] -= cap
            start[1] -= cap
            
            # 반복문 n-1부터 시작이기 때문에 i+1
            answer += (i+1) * 2
        
    
    return answer