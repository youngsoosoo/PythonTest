def solution(keymap, targets):
    answer = []
    for i in targets:
        a=0
        for j in i:
            result=[]
            for k in keymap:
                if j in k:
                    result.append(k.index(j)+1)
            if result:
                a += min(result)
        print()
        if a == 0:
            answer.append(-1)
        else:
            answer.append(a)
            
    return answer