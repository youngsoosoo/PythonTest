### 문제 인식 ###
# 어피치의 양궁 점수가 주어집니다.
# 어피치와 라이언이 해당 점수에 쏜 화살의 수가 같다면 어피치가 그 점수를 얻게 됩니다.
# 또한 최종 점수가 같다면 어피치가 우승하게 됩니다.
# 이때, 라이언이 가장 큰 점수차로 우승하기 위해 맞춰야할 과녁을 리턴해주세요.
# 가장 큰 점수 차로 우승할 수 있는 방법이 여러 가지일 경우 가장 낮은 점수를 더 많이 맞춘 경우를 리턴해주세요.
### 문제 해결 방법 ###
# BFS를 통해 문제 풀이를 진행해야 할 거 같습니다.

from collections import deque
def solution(n, info):
    answer = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0
    
    while q:
        focus, arrow = q.popleft()
        
        if sum(arrow) == n:
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:  # 라이언이 이기면
                gap = lion - apeach
                if maxGap > gap:
                    continue
                elif maxGap < gap:
                    maxGap = gap  # 최대점수차 갱신
                    answer.clear()
                answer.append(arrow)  # 최대점수차를 내는 화살상황 저장
        
        elif sum(arrow) > n:  # 종료조건 2) 화살 더 쏜 경우
            continue
        
        elif focus == 10:  # 종료조건 3) 화살 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))
        
        else:  # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus]+1 
            q.append((focus+1, tmp))  # 어피치보다 1발 많이 쏘기
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1, tmp2))  # 0발 쏘기
    
    if not answer:
        return [-1]
    elif len(answer) == 1:
        return answer[0]
    else:
        return answer[-1]
    
    return answer