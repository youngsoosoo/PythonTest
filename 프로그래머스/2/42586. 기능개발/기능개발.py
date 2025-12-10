import math
def solution(progresses, speeds):
    answer = []
    result = []
    
    for i in range(len(progresses)):
        answer.append(((100 - progresses[i] + speeds[i] - 1) // speeds[i]))
    
    num = 0
    for i in answer:
        if num < i:
            num = i
            result.append(1)
        else:
            result[-1] += 1
            
    
    return result