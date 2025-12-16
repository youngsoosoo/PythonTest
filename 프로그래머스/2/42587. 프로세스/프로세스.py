from collections import deque
def solution(priorities, location):
    answer = []
    
    queue = deque((i, j) for i, j in enumerate(priorities))
    while queue:
        process = queue.popleft()
        
        if queue and any(process[1] < q[1] for q in queue):
            queue.append(process)
        else:
            answer.append(process)
    
    for i, j in answer:
        if i == location:
            return answer.index((i,j)) + 1