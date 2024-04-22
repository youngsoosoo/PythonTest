def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
    
    div = s//n
    mod = s%n
    
    for i in range(n):
        answer.append(div)
        
    if mod:
        for i in range(n):
            answer[i] += 1
            mod -= 1
            if not mod:
                break
        
    return sorted(answer)