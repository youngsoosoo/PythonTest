def solution(n, k):
    answer = 0
    
    def change(n, q):
        rev_base = ''

        while n > 0:
            n, mod = divmod(n, q)
            rev_base += str(mod)

        return rev_base[::-1]
    
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    prime = change(n, k)
    
    s = []
    result = ''
    for p in prime:
        if p != '0':
            s.append(p)
        else:
            if s:
                result = ''.join(s)
                if is_prime(int(result)):
                    answer+=1
                s=[]
        
    a = ''.join(s)
    if len(a) > 0 and is_prime(int(a)):
        answer+=1
    
    return answer