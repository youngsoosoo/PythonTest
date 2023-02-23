def solution(s, skip, index):
    answer = ''
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    for i in skip:
        if i in alpha:
            alpha = alpha.replace(i, "")
    
    for i in s:
        a = alpha[(alpha.index(i) + index) % len(alpha)]
        answer+=a
    
    return answer