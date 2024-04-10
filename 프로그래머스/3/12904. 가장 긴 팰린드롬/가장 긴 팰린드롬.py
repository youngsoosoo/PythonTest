def solution(s):
    
    for i in range(len(s), 1, -1):
        for j in range(len(s)-i+1):
            a = j
            b = i+j-1
            isBoolean = True
            while a<=b:
                
                if s[a] != s[b]:
                    isBoolean = False
                    break
                a+=1
                b-=1
            if isBoolean:
                return i
    
    return 1