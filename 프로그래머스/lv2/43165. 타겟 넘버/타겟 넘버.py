from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque([[numbers[0], 0], [-1 * numbers[0], 0]])
    i=0
    
    while q:
        x, i = q.popleft()
        i += 1
        
        if i < len(numbers):
            q.append([x+numbers[i], i])
            q.append([x-numbers[i], i])
        elif x == target:
            answer+=1

    return answer