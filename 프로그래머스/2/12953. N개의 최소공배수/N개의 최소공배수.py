def solution(arr):
    answer = arr[0]
    
    for i in arr[1:]:
        answer = lcm(answer, i)
        
    return answer

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)