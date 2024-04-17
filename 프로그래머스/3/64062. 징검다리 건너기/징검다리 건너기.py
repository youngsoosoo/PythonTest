import sys
def solution(stones, k):
    answer = 0
    
    start, end = 1, max(stones)
    
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
            else:
                cnt = 0
                
            if cnt >= k:
                break
        
        if cnt < k:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    
    return answer