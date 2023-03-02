def solution(survey, choices):
    answer = ''
    # 0:[R, T] 1:[C, F] 2:[J, M] 3:[A, N]
    
    result = {"R" : 0,"T" : 0,"C" : 0,"F" : 0,"J" : 0,"M" : 0,"A" : 0,"N" : 0 }
    
    for s,c in zip(survey,choices):
        if c>4:     result[s[1]] += c-4
        elif c<4:   result[s[0]] += 4-c
        
    li = list(result.items())
    
    for i in range(0, 8, 2):
        if li[i][1] >= li[i+1][1]:
            answer+=li[i][0]
        else:
            answer+=li[i+1][0]
            
    return answer