def solution(progresses, speeds):
    answer = []
    result=0
    for i in range(len(progresses)):
        a = 100 - progresses[i]
        if a%speeds[i] > 0:
            a = a//speeds[i] + 1
        else:
            a = a//speeds[i]
        if len(answer)>0 and result == max(a, result):
            answer[-1] += 1
            continue
        result = a
        answer.append(1)
    return answer