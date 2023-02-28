def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if budget <= 0:
            break
        budget-=i
        answer+=1
    if budget < 0:
        answer-=1
    return answer