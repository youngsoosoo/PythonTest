def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    result=[]
    for i in score:
        result.append(i)
        if len(result) == m:
            answer+=min(result)*m
            result=[]

    return answer