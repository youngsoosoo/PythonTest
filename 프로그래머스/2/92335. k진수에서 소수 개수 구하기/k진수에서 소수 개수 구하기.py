
answer = ''

def solution(n, k):
    result = 0
    
    answer = findNumber(n, k)
    answer = answer.split('0')
    for i in answer:
        if len(i) == 0:
            continue
        if int(i) < 2:
            continue
        
        if is_prime_number(int(i)):
            result += 1
    
    return result

def is_prime_number(n):
    end = int(n**(1/2))
    for i in range(2, end+1):
        if n % i == 0:
            return False
    
    return True

def findNumber(n, k):
    global answer
    while n:
        answer += str(n % k)
        n //= k
    
    return answer[::-1]