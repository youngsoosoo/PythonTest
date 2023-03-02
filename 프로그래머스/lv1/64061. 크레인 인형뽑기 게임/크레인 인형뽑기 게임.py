def solution(board, moves):
    answer = 0
    result=[]
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                result.append(j[i-1])
                if len(result) > 1 and result[-1] == result[-2]:
                    result.pop()
                    result.pop()
                    answer+=2
                j[i-1]=0
                break
    return answer