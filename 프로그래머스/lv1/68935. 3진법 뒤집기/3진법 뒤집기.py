def solution(n):
    answer = ''

    while n>0:
        a = n % 3
        n = n // 3
        answer += str(a)
    
    return int(answer, 3)