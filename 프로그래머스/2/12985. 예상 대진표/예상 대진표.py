def solution(n,a,b):
    answer = 0
    
    while abs(a-b) >= 1:
        # 현재 N//2의 수보다 둘 다 작으면 만난다.
        
        answer += 1
        if a % 2 != 0:
            a += 1
        if b % 2 != 0:
            b += 1
        a //= 2
        b //= 2
        
        
    
    return answer