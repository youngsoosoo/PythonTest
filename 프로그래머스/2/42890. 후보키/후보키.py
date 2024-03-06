from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    arr = []
    # 모든 속성 조합 탐색
    for i in range(1, col+1):
        arr.extend(combinations(range(col), i))
        
    # 유일성을 만족하는 조건 탐색
    unique = []
    for i in arr:
        s = [tuple(j[k] for k in i) for j in relation]
        if row == len(set(s)):
            unique.append(i)
    
    # 최소성을 만족하는 조건 탐색
    least = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                least.discard(unique[j])
        
    return len(least)