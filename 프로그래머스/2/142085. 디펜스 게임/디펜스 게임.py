from heapq import heappush, heappop
def solution(n, k, enemy):
    answer = len(enemy)
    
    if k >= answer:
        return answer
    
    q = []
    
    for i in range(answer):
        heappush(q, enemy[i])
        if len(q) > k:
            small = heappop(q)
            if small > n:
                return i
            n -= small
    return answer