def solution(clothes):
    answer = 1
    
    dic = {}
    
    for n, t in clothes:
        dic.setdefault(t, []).append(n)
        
    for value in dic.values():
        answer *= (len(value) + 1)
        
    return answer - 1