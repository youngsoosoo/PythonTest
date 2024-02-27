def solution(n, t, m, p):
    answer = ''
    
    # n을 base 진수로 진수 변환
    def convert(n, base):
        arr = "0123456789ABCDEF"
        q, r = n // base, n % base
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]

    
    for i in range(t*m):
        c = convert(i, n)
        answer += c
        
    ans = ''
    for i in answer[p-1:t*m:m]:
        ans+=i
        
    return ans