def solution(k, tangerine):
    answer = 0
    cnt = 0
    
    dic = {}
    
    for i in tangerine:
        dic[i] = dic.get(i, 0) + 1
            
    dicItems = sorted(dic.values(), reverse=True)
    
    for i in dicItems:
        if (cnt >= k):
            return answer
        
        cnt += i
        answer += 1
    
    return answer