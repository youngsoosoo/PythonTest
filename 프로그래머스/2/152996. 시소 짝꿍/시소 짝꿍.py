from collections import Counter

def solution(weights):
    answer = 0

    counter = Counter(weights)
    for k, v in counter.items():
        if v>1:
            answer += v*(v-1)//2
    weights = set(weights)
    
    for i in weights:
        if i*2/3 in weights:
            answer += counter[i] * counter[i*2/3]
        if i*2/4 in weights:
            answer += counter[i] * counter[i*2/4]
        if i*3/4 in weights:
            answer += counter[i] * counter[i*3/4]
    
    return answer