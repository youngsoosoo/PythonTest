def solution(N, stages):
    fail = dict()
    user = len(stages)
    
    for i in range(1, N+1):
        if user != 0:
            cnt = stages.count(i)
            a = cnt / user
            fail[i] = a
            
            user-=cnt
        else:
            fail[i]=0

    return sorted(fail, key=lambda x:fail[x], reverse=True)