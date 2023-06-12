### 문제 인식 ###
# 이모티콘 할인 행사를 할 때 1. 가입자는 최대한 늘리고 2. 판매액은 최대한 늘려야합니다.
# 1번이 우선 2번이 다음입니다.
# 3. 사용자들은 자신의 기준에 따라 할인하는 이모티콘을 모두 구매합니다.
# 4. 이모티콘을 구입할 때 그 합이 이모티콘 플러스 서비스보다 비싸다면 대신 서비스에 가입합니다.
# 행사 목적을 최대한 달성했을 대 이모티콘 플러스 서비스 가입 수와 이모티콘 매출액을 return
### 문제 해결 방법 ###
# O(n^2)이상 O(n^3)이하 가능, 완전 탐색으로 가능.
# 1. 각 이모티콘에 적용해주어야 할 할인율을 구합니다.
# 1-1. 할인율이 작은 것부터 큰것까지 서비스 가입자 수와 이모티콘 판매 수익을 구해서 저장.
# 

from itertools import product

def solution(users, emoticons):
    
    answer = []
    discount = []
    
    n, m = len(users), len(emoticons)
    
    # 모든 할인율의 조합
    for i in product([10, 20, 30, 40], repeat=m):
        
        arr = [0, 0]
        # 유저를 기준으로 값 찾기
        for per, money in users:
            value = 0
            for emoticon, discount in zip(emoticons, i):
                if discount >= per:
                    value += emoticon*(100-discount)//100
            if money <= value:
                arr[0] += 1
            else:
                arr[1] += value
        answer.append(arr)
    answer.sort(key=lambda x:(x[0], x[1]))

    return answer[-1]