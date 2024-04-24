from collections import Counter
def solution(participant, completion):
    answer = ''
    
    dicP = Counter(participant)
    dicC = Counter(completion)
    
    for p in dicP.keys():
        if p not in dicC or dicP[p] != dicC[p]:
            return p
    
    return answer