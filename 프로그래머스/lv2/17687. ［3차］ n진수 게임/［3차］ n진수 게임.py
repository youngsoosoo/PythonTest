def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):
    answer = ''
    s = '0'
    i=0
    while len(s) < t*m:
        s+=convert(i, n)
        i+=1
    print(s)
    for i in range(p, len(s), m):
        if i < len(s):
            answer+=s[i]
    return answer[:t]