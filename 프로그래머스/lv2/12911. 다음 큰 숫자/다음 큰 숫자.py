def solution(n):
    answer = 0
    a = bin(n)[2:].count('1')
    answer = n
    while True:
        answer+=1
        if bin(answer)[2:].count('1') == a and n < answer:
            break
    return answer