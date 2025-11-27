def solution(n):
    
    if n < 3:
        return n
        
    li = [1, 2]
    
    for i in range(2, n):
        li.append((li[i-1] + li[i-2]) % 1234567)
    
    return li[-1]