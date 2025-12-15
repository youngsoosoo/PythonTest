def solution(s):
    answer = []
    
    s = s[2:-2].split('},{')
    li = sorted([list(map(int, i.split(','))) for i in s], key=len)
    
    for i in li:
        for j in i:
            if j not in answer:
                answer.append(j)
    
    return answer