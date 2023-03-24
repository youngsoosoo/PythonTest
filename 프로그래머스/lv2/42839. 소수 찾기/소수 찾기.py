from itertools import permutations
def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    arr=set()
    
    for i in range(1, len(numbers)+ 1):
        for j in permutations(numbers, i):
            arr.add(int(''.join(j)))
    for i in arr:
        if isprime(i):
            answer+=1

    return answer