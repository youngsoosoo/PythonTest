def solution(s):
    answer = 0
    
    for i in range(len(s)):
        newList = s[i:] + s[:i]
        q = [newList[0]]
        for j in range(1, len(s)):
            if len(q) != 0:
                if q[-1] == '{' and newList[j] == '}' or q[-1] == '[' and newList[j] == ']' or q[-1] == '(' and newList[j] == ')':
                    q.pop()
                    continue
            q.append(newList[j])
                    
        if not q:
            answer += 1
    
    return answer