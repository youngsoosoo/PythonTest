def solution(n,a,b):
    answer = 0
    
    while abs(a-b) >= 1:
        answer += 1
        a, b = (a+1) // 2, (b+1) // 2
        
        
    
    return answer