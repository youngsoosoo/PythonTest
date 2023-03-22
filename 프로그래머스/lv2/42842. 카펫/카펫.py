def solution(brown, yellow):
    answer = []
    a = brown + yellow
    for i in range(1, int(a**1/2) + 1):
        if a % i == 0 :
            x = a//i
            if x*2 + i*2 - 4 == brown and x>=i:
                answer.append(x)
                answer.append(i)
        
    return answer