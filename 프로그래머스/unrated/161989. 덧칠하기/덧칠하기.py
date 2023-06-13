### 문제 인식 ###
# 총 길이가 N인 벽이 있습니다.
# 이 벽에서 주어진 section이 있고 한 번 칠할 때 M의 길이 만큼 칠할 수 있습니다.
# 하지만 모든 구역을 칠해야하기 때문에 페인트칠을 해야하는 최소 횟수를 구하시오,
### 문제 해결 방법 ###
# O(NlogN)
# 1. O(NlogN)보다 작은 수를 속도로 구하기 위해 하나의 반복문 사용
# 2. a가 i+m보다 작다면 아직 칠하지 않은 부분이므로 다시 칠하고 수를 계산.
# 3. 이때, section을 순회하며 한 번에 칠할 수 있는 것인 m을 더해줌

def solution(n, m, section):
    answer = 0
    
    a = 0
    
    # 1
    for i in section:
        # 2
        if a <= i:
            # 3
            a=i+m
            answer+=1
    
    return answer