import sys
def solution(sequence):
    answer = sys.maxsize * -1
    
    a, a_min, b, b_min = 0, 0, 0, 0
    plus = 1
    
    for s in sequence:
        a += s * plus
        b += s * plus * -1
        
        answer = max(answer, a-a_min, b-b_min)
        
        a_min = min(a_min, a)
        b_min = min(b_min, b)
        
        plus *= -1
    
    return answer