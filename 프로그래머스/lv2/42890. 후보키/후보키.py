### 문제 인식 ###
# 후보키의 최대 개수를 구해야합니다.
# 후보키는 유일성과 최소성을 만족해야합니다.
# 학번은 독립적으로 존재해도 후보키의 조건을 만족합니다.
# 학번 + 이름은 학번만으로도 후보키의 조건을 만족하기 때문에 유일성을 만족하지 않습니다.
# 이름 + 전공 + 학년은 유일성은 만족하지만 이 예시에서는 학년이 포함되든 안 되는 유일성을 만족하기 때문에
# 학년을 뺀 이름 + 전공만으로도 후보키의 조건을 만족합니다.
### 문제 해결 ###
# 먼저 모든 조합을 찾습니다.
# 유일성을 만족하는 것을 찾습니다.
# 최소성을 만족하는 것을 찾습니다.
# 남은 것을 리턴해줍니다.

from itertools import combinations
def solution(relation):
    answer = 0
    
    row = len(relation)
    col = len(relation[0])
    
    #모든 좋바
    result = []
    for i in range(1, col+1):
        result.extend(combinations(range(col), i))

    #유일성
    unique = []
    for i in result:
        temp = [tuple([r[j] for j in i]) for r in relation]
        if len(set(temp)) == row:
            unique.append(i)
    
    #최소성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    
    return len(answer)