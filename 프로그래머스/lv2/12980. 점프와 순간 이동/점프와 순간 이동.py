def solution(n):
    ans = 1
    while n > 1:
        ans += n%2
        n = n//2
    
    return ans