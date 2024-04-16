def solution(scores):
    answer = 0
    
    x, y = scores[0]
    score = x+y
    scores.sort(key=lambda x:(-x[0], x[1]))
    
    max_y1 = 0
    
    for x1, y1 in scores:
        
        if x1 > x and y1 > y:
            return -1
        
        if max_y1 <= y1:
            
            max_y1 = y1
            if x1 + y1 > score:
                answer += 1
    
    return answer + 1