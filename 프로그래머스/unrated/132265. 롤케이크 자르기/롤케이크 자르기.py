from collections import Counter

def solution(topping):
    answer = 0
    s = set()
    dic = Counter(topping)
    
    for i in topping:
        s.add(i)
        dic[i] -= 1
        if dic[i] == 0:
            dic.pop(i)
        if len(s) == len(dic):
            answer+=1
            
    return answer