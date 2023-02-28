def solution(a, b, n):
    answer = 0    
    while n >= a:
        c = n%a
        n = (n//a)*b
        answer+=n
        n+=c
        print(answer, n, c)
        
    return answer