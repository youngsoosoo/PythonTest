def solution(n):
    answer = []
    
    
    def recur(n, start, end, assistant):
        if n == 1:
            answer.append([start, end])
        else:
            recur(n-1, start, assistant, end)
            recur(1, start, end, assistant)
            recur(n-1, assistant, end, start)
            
        
    recur(n, 1, 3, 2)
    
    return answer