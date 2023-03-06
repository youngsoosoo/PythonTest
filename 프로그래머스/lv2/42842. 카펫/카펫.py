def solution(brown, yellow):
    answer = []
    t = brown + yellow
    for i in range(1, t+1):
        if t%i == 0:
            if 2*i + 2*(t//i) - 4 == brown and t//i >= i:
                answer.append(t//i)
                answer.append(i)
    return answer