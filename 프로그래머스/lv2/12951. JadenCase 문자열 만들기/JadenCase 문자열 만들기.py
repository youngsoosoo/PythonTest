def solution(s):
    answer = ''
    arr = list(s.split(' '))
    a=[]
    for i in arr:
        i = i.capitalize()
        a.append(i)
    answer = ' '.join(a)
    return answer