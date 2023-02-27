def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] != True:
            absolutes[i]*=-1
    answer=sum(absolutes)
    return answer