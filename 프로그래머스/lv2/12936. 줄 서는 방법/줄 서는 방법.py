def solution(n, k):
    answer = [i for i in range(1, n+1)]
    factorial = [1] * n
    
    for i in range(1, n):
        factorial[i] = factorial[i-1] * i

    k -= 1 
    result = []
    for i in range(n-1, -1, -1):
        idx = k // factorial[i]
        k %= factorial[i]
        result.append(answer[idx])
        answer.pop(idx)
    
    return result