import heapq as hq

def solution(scoville, K):
    answer = 0
    
    heap = []
    
    for i in scoville:
        hq.heappush(heap, i)
    
    while heap[0] < K:
        hq.heappush(heap, hq.heappop(heap) + hq.heappop(heap)*2)
        
        if len(heap) == 1 and heap[0] < K:
            return -1
        
        answer+=1
    
    return answer