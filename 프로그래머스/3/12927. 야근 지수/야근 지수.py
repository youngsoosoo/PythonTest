import heapq
def solution(n, works):
    if n >= sum(works):
        return 0
    
    works = [-work for work in works]
    heapq.heapify(works)
    
    for i in range(n):
        work = heapq.heappop(works)
        work += 1
        heapq.heappush(works, work)
    
    return sum([work**2 for work in works])