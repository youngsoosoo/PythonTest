def solution(operations):
    answer = [0, 0]
    q = []
    for operation in operations:
        s, n = operation.split()
        if s == 'I':
            q.append(int(n))
        elif s == 'D' and len(q) != 0:
            if int(n) == -1:
                q.pop(q.index(min(q)))
            else:
                q.pop(q.index(max(q)))
    
    if len(q) != 0:
        answer = [max(q), min(q)]
    return answer