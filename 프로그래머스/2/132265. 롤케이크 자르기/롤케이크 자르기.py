from collections import Counter
def solution(topping):
    answer = 0
    
    dic = Counter(topping)
    setDic = set()
    
    for i in topping:
        dic[i] -= 1
        setDic.add(i)
        
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(setDic):
            answer += 1
    
    
    return answer