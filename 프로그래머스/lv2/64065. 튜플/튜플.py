def solution(s):
    a=''
    result = []
    for i in list(s[1:-1]):
        if i.isnumeric() or i == ',':
            a += i
        if i == '}':
            a = a.strip(',')
            result.append(list(map(int, a.split(','))))
            a = ''
            
    result.sort(key=len)
    
    if len(result) == 1:
        return result[0]
    answer = [result[0][0]]
    for i in range(len(result)):
        for j in result[i]:
            if j not in answer:
                answer.append(j)
        
    return answer