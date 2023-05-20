### 문제 인식 ###
# 2M, 3M, 4M를 기준으로 양쪽에 최대 2명이 앉을 수 있습니다.
# 탑승한 사람의 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같다면 시소 짝꿍입니다.
# weight * M
### 문제 해결 ###
# itertools를 사용해 두자리로 가능한 모든 경우의 수를 찾아줍니다. (시간초과)
# Counter 객체를 사용해 각 요소의 개수를 세어줍니다.
# 2개 이상인 것을 찾아 answer에 더해주게 되는데
# 이때 2개가 아니라 3개이면 모든 경우의수를 더해주기 위해 b*(b-1)//2를 더해줍니다.
# 2:3, 2:4, 3:4 비율로 짝이 가능한 경우를 확인합니다.
# 두 무게를 가지는 사람 수를 곱해주고, 이를 answer에 더해준다.
from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    
    for a, b in counter.items():
        if b >= 2:
            answer += b*(b-1)//2
    weights = set(weights)
    for w in weights:
        if w*2/3 in weights:
            answer+= counter[w*2/3] * counter[w]
        if w*2/4 in weights:
            answer+= counter[w*2/4] * counter[w]
        if w*3/4 in weights:
            answer+= counter[w*3/4] * counter[w]

    return answer