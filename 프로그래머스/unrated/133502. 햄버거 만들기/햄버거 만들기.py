def solution(ingredient):
    answer = 0
    result=[]
    for i in ingredient:
        result.append(i)
        if len(result) > 3 and result[-1] == 1 and result[-2] == 3 and result[-3] == 2 and result[-4] == 1:
            result.pop()
            result.pop()
            result.pop()
            result.pop()
            answer+=1
    return answer