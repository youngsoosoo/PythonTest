import math

def solution(brown, yellow):
    answer = [0, 0]
    
    by = brown + yellow

    for i in range(3, int(math.sqrt(by)) + 1):
        if by % i == 0 and (by // i - 2) * (i - 2) == yellow:
            return [by // i, i]