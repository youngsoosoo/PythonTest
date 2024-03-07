from collections import deque
def solution(queue1, queue2):
    answer = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    li1 = len(queue1)
    li2 = len(queue2)
    limit = (li1 + li2)*2
    
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    result = (sum_queue1 + sum_queue2) // 2
    
    while True:
        
        if answer == limit :
            return -1
        
        if sum_queue1 == result and sum_queue2 == result:
            return answer
        
        if sum_queue1 < result:
            a = queue2.popleft()
            queue1.append(a)
            sum_queue1+=a
            sum_queue2-=a
        elif sum_queue2 < result:
            a = queue1.popleft()
            queue2.append(a)
            sum_queue1-=a
            sum_queue2+=a
            
        answer+=1
        
    
    return answer