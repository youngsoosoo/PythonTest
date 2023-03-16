def solution(n, times):
    answer = 0
    start, end = min(times), max(times)*n
    
    while start <= end:
        mid = (start + end)//2
        cnt = 0
        
        for i in times:
            cnt += mid//i
            
            if cnt >= n:
                break
        
        if cnt < n:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
            
            
    return answer