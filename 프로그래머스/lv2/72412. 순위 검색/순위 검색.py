### 문제 이해 ###
# 개발팀에서 궁금해하는 문의사항에 맞게 문의 조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return
# 배열의 크기 1~50000이하
# 개발언어, 직군, 경력, 소울푸드, 코딩테스트 점수
### 문제 해결 방법 ###
# info - 50,000 이하, query - 100,000 이하, O(nlogn) 이하.
# 1. info 안의 문자열을 공백을 기준으로 분리합니다. ( ex ['java', 'backend', 'junior', 'pizza', '150'] )
# 2. 분리한 것 중, 앞의 4부분(java,backend..)을 키값으로, 마지막부분(150)을 value값으로 분리 합니다.
# 3. 키값들로 만들 수 있는 모든 조합을 생성합니다. (combinations 이용)
# 4. 이 조합으로 딕셔너리를 생성합니다. 해당 키값이 딕셔너리에 이미 존재하면 value값을 그 키의 value값에 추가합니다.
#    { 'javabackendjuniorpizza' : [150...] , 'java' : [100...] , ... } 식으로 생성이 되겠죠?
# 5. 딕셔너리의 각 원소마다 value값들을 기준으로 정렬합니다. [100,150,200...]식으로 되도록
# 6. query도 마찬가지로 분리합니다. ( query에는 and와 -도 있기 때문에 제거를 하여 info와 같은 형식으로 만듭니다. )
# 7. 이제 query를 한바퀴 돌면서, info딕셔너리를 탐방하게 되는데, query의 key값이 info딕셔너리의 키값으로 존재하면 그 info딕셔너리의 value값들을 가져옵니다.
# 8. 가져온 점수값에서 기준 점수값을 넘는 것들의 개수를 이분탐색을 통해 구하면 됩니다.

from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dict = {}

    for i in range(len(info)):
        infol = info[i].split()  # info안의 문자열을 공백을 기준으로 분리
        mykey = infol[:-1]  # info의 점수제외부분을 key로 분류
        myval = infol[-1]  # info의 점수부분을 value로 분류

        for j in range(5):  # key들로 만들 수 있는 모든 조합 생성
            for c in combinations(mykey, j):
                tmp = ''.join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(myval))  # 그 조합의 key값에 점수 추가
                else:
                    info_dict[tmp] = [int(myval)]
    
    for k in info_dict:
        info_dict[k].sort()  # dict안의 조합들을 점수순으로 정렬

    for qu in query:  # query도 마찬가지로 key와 value로 분리
        myqu = qu.split(' ')
        qu_key = myqu[:-1]
        qu_val = myqu[-1]

        while 'and' in qu_key:  # and 제거
            qu_key.remove('and')
        while '-' in qu_key:  # - 제거
            qu_key.remove('-')
        qu_key = ''.join(qu_key)  # dict의 key처럼 문자열로 변경

        if qu_key in info_dict:  # query의 key가 info_dict의 key로 존재하면
            scores = info_dict[qu_key]

            if scores:  # score리스트에 값이 존재하면
                enter = bisect_left(scores, int(qu_val))

                answer.append(len(scores) - enter)
        else:
            answer.append(0)

    return answer