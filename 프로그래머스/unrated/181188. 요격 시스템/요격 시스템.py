### 문제 인식 ###
# 모든 폭격 미사일을 최소 비용으로 요격해야 합니다.
# A 나라 미사일은 (s, e) 형태로 X 축에 평행하 형태의 미사일입니다.
# B 나라 미사일은 x좌표에서 Y축에 수평이 되도록 관통하는 미사일을 발사합니다.
### 문제 해결 ###
# 1. 주어진 targets를 x[1], x[0] 오름차순으로 정렬해줍니다.
# 2. s와 e를 0으로 초기화 해줍니다.
# 3. 이전 e와 현재 s가 겹치는 구간이 있가면 +1을 해줍니다.
def solution(targets):
    
    answer = 0
    
    # 1
    targets.sort(key=lambda x:(x[1],x[0]))
    
    # 2
    s, e = 0, 0
    
    # 3
    for target in targets:
        if target[0] >= e:
            answer += 1
            e = target[1]
            
    return answer