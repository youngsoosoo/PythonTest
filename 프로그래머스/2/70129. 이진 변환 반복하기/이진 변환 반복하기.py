import math
def solution(s):
    answer = [0, 0]
    
    while s != '1':
        sLen = len(s)
        sCnt = s.count('1')
        answer[1] += sLen - sCnt
        s = bin(sCnt)[2:]
        answer[0] += 1
        
    
    return answer