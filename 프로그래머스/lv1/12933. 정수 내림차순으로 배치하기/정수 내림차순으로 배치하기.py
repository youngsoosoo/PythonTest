def solution(n):
    answer = ''
    n = str(n)
    a=[]
    for i in range(len(n)):
        a.append(n[i])
    a.sort(reverse=True)
    for i in a:
        answer+=i
    answer = int(answer)
    return answer