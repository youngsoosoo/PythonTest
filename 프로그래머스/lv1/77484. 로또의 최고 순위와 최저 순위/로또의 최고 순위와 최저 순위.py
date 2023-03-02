def solution(lottos, win_nums):
    answer = []
    cnt=0
    for i in lottos:
        if i in win_nums:
            cnt+=1

    if cnt+lottos.count(0) == 0:
        answer.append(6)
    else:
        answer.append(7-(cnt+lottos.count(0)))
        
    if cnt == 0:
        answer.append(6)
    else:
        answer.append(7-cnt)
    return answer