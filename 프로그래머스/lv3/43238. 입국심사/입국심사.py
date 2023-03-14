def solution(n, times):
    start, end = 1, max(times)*n
    while start <= end:
        mid = (start + end)//2
        cnt = 0
        
        for i in times:
            if i <= mid:
                cnt += mid//i
        
        if cnt < n:
            start = mid + 1
        else:
            end = mid - 1
            
    return start