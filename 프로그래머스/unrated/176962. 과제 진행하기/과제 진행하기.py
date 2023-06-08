### 문제 인식 ###
# 과제를 해야합니다.
# 하지만 진행중이어도 다음 과제가 시작한다면
# 멈추고 새로운 과제를 시작해야합니다.
### 문제 해결 방법 ###
# 1. 먼저 시작 시간과 과제하는데 걸리는 시간을 모두 정수형으로 변환해줍니다.
# 2. 시작 시간을 기준으로 정렬해줍니다.
# 3. plans의 길이만큼 반복문을 실행해줍니다.
# 4. 현재 반복한 횟수가 마지막인 경우 과제를 먼저 완료해줍니다.
# 5. 현재 과제와 다음 과제들에 대한 선언을 해줍니다.
# 6. 과제가 끝났을 때와 안 끝났을 때를 기준으로 과제가 끝났으면 answer에
#    안 끝났으면 result에 추가해줍니다.
# 7. 과제가 끝났을 때 cnt가 남아있다면 가장 최근에 중단한 과제를 마무리해줍니다.
# 8. 마지막으로 안 끝나 과제들을 최근 중단한 순으로 마무리 해줍니다.
def solution(plans):
    answer = []
    
    # 1
    for i in range(len(plans)):
        time, minutes = map(int, plans[i][1].split(':'))
        total = time*60 + minutes
        plans[i][1] = total
        plans[i][2] = int(plans[i][2])
        
    # 2
    plans.sort(key=lambda x:x[1])
    
    result = []
    
    # 3
    for i in range(len(plans)):
        
        # 4
        if i == len(plans) - 1:
            plans[i][2] = 0
            answer.append(plans[i][0])
            break
        
        # 5
        name, time, minutes = plans[i][0], plans[i][1], plans[i][2]
        nname, ntime, nminutes = plans[i+1][0], plans[i+1][1], plans[i+1][2]
        
        cnt = ntime - time
        
        # 6
        # 과제가 끝났을 때
        if cnt >= minutes:
            cnt -= minutes
            plans[i][2] = 0
            answer.append(name)
            
            # 7
            while cnt > 0 and result:
                a, b, c = result.pop()
                if cnt >= c:
                    cnt -= c
                    answer.append(a)
                else:
                    result.append([a, b, c-cnt])
                    cnt = 0
        #과제가 안 끝났을 때
        else:
            plans[i][2] -= cnt
            cnt = 0
            result.append(plans[i])
    
    # 8
    while result:
        a, b, c = result.pop()
        answer.append(a)
    
    return answer
