def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

def solution(numer1, denom1, numer2, denom2):
    a = numer2*denom1 + numer1*denom2
    b = denom1 * denom2
    c = gcd(a, b)
    
    
    return [a//c, b//c]