def solution(s):
    answer = ''
    
    bol = True
    for i in s:
        if i == ' ':
            bol = True
            answer += i
        else:
            if bol:
                bol = False
                answer += i.upper()
            else:
                answer += i.lower()
    
    return answer