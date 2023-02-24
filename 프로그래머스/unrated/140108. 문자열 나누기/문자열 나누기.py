def solution(s):
    answer = 0
    str1 = ""
    str2 = ""
    a, b = 0, 0
    q=0
    while q < len(s):
        first = s[q]
        for i in range(q, len(s)):
            if first == s[i]:
                a+=1
            else:
                b+=1
            q+=1
            if a == b:
                answer += 1
                break
            elif i == len(s)-1:
                answer+=1
        
    return answer