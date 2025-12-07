def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    for i, c in enumerate(citations):
        
        if c >= i+1:
            answer = i + 1
        else:
            break
    return answer
            
