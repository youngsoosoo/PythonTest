### 문제 인식 ###
# [dia, iron, stone] 순으로 주어진 picks의 곡괭이 개수가 있습니다.
# minerals는 캐야할 광물입니다. 하나의 곡괭이는 무조건 최대 5개의 광물을 캘 수 있습니다.
# 각 곡괭이마다 피로도가 존재하는데 이 피로도를 다 쓰게되면 다른 곡괭이로 바꿔야합니다.
# 이때 주어진 minerals를 모두 캘 때까지 필요한 최소한의 피로도를 구하시오.
### 문제 해결 ###
# 그리디 알고리즘을 통해 다음 다섯개를 캘 때 가장 작은 피로도가 나올 수 있도록 풀이.(X)
# 가장 먼저 곡괭이의 개수에 맞춰 리스트를 다시 만들어주고,
# 광물의 수를 5개의 단위마다 끊어 세어준다.
# 정렬을 통해 dia, iron, stone 순으로 가장 많은 것부터 피로도를 세어준다면
# 피로도가 최소로 나온다.
from collections import deque
def solution(picks, minerals):
    answer = 0
    pick_count = sum(picks) * 5

    if len(minerals) > pick_count:
        minerals = minerals[:pick_count]
    mineral = [[0, 0, 0] for i in range(10)]
    
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            mineral[i//5][0] += 1
        elif minerals[i] == "iron":
            mineral[i//5][1] += 1
        else:
            mineral[i//5][2] += 1
    mineral.sort(key=lambda x:(x[0], x[1], x[2]), reverse=True)
    
    for d, i, s in mineral:
        if picks[0] > 0:
            answer += d + i + s
            picks[0] -= 1
        elif picks[1] > 0:
            answer += 5 * d + i + s
            picks[1] -= 1
        else:
            answer += 25 * d + 5 * i + s
    
    return answer