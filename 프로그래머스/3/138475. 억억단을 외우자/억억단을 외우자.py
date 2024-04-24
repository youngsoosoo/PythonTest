def solution(e, starts):
    
    num = [0] * (e+1)
    
    for i in range(2, e+1):
        if i*i <= e:
            num[i]+=1
        for j in range(i+1, e+1):
            n = i * j
            if n > e:
                break
            num[n] += 2
    
    answer = [0] * (e+1)
    answer[e] = e
    
    for i in reversed(range(0, e)):
        if num[i] >= num[answer[i+1]]:
            answer[i] = i
        else:
            answer[i] = answer[i+1]
    
    return [answer[start] for start in starts]