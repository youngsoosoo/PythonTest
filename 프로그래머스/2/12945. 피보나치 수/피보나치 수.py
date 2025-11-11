def solution(n):
    
    # DP 문제로 풀이해야함
    # (n+2) = n + (n+1)
    
    li = [0, 1]
    
    for i in range(2, n+1):
        li.append((li[i-1] + li[i-2]) % 1234567)
    
    return li[n]