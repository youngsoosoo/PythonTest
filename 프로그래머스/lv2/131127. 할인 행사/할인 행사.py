from collections import Counter

def solution(want, number, discount):
    answer = 0
    result = dict(zip(want, number))
    for i in range(len(discount)-9):
        dic = Counter(discount[i:i+10])
        if dic == result:
            answer+=1
    return answer