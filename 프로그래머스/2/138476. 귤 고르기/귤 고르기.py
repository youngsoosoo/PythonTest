from collections import Counter
def solution(k, tangerine):
    answer = 0
    
    counter = Counter(tangerine)
    sorted_keys = [key for key, _ in counter.most_common()]
    for i in sorted_keys:
        if k <= 0:
            break
        k -= counter[i]
        answer+=1
        
    return answer