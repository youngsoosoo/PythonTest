def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    arr.sort()
    while len(arr) > 1:
        a, b = arr.pop(), arr.pop()
        arr.append(lcm(a, b))
    return arr[0]