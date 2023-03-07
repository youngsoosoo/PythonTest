from collections import deque
def solution(s):
    answer=0
    s = list(s)
    s = deque(s)
    for i in range(len(s)):
        a = ''.join(s)
        s = deque(list(a))
        si=''
        for i in a:
            si += i
            if '()' in si or '{}' in si or '[]' in si:
                si=si.replace('()', '')
                si=si.replace('{}', '')
                si=si.replace('[]', '')
        if si == '':
            answer+=1
        
        s.append(s.popleft())
        
    return answer