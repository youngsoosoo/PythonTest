from itertools import permutations
def solution(user_id, banned_id):
    result = []
    
    for i in permutations(user_id, len(banned_id)):
        cnt = 0
        for a, b in zip(i, banned_id):
            flag = 1
            if len(a) == len(b):
                for c, d in zip(a, b):
                    if d == '*':
                        continue
                    elif c != d or len(c) != len(d):
                        flag=0
                        break

                if not flag:
                    break
                else:
                    cnt+=1
        
        if cnt == len(banned_id) and set(i) not in result:
            result.append(set(i))
    
    return len(result)