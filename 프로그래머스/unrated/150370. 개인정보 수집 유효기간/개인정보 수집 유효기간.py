def solution(today, terms, privacies):
    answer = []
    
    t = list(map(int, today.split('.')))
    terms1={}
    
    for i in terms:
        a, b = i.split()
        terms1[a] = int(b)
    for i in range(len(privacies)):
        a, b = map(str, privacies[i].split())
        a = list(map(int, a.split('.')))
        b = terms1[b]
        a[1]+=b
        a[2]-=1
        if a[2] < 1:
            a[1] -= 1
            a[2] = 28
        while a[1] > 12:
            a[1]-=12
            a[0]+=1
        if a[0] < t[0]:
            answer.append(i+1)
        elif a[0] == t[0]:
            if a[1] < t[1]:
                answer.append(i+1)
            elif a[1] == t[1]:
                if a[2] < t[2]:
                    answer.append(i+1)
        print(a)
    return answer