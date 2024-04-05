def solution(n, cores):
    
    if n <= len(cores):
        return n
    
    n -= len(cores)
    left, right = 1, n * max(cores)
    
    while left < right:
        mid = (left+right)//2
        
        total = 0
        for c in cores:
            total += mid // c
            
        if total >= n:
            right = mid
        else:
            left = mid+1

    for c in cores:
        n -= (right-1) // c
        
    for i in range(len(cores)):
        if right%cores[i]==0:
            n-=1
            if n==0:
                return i+1