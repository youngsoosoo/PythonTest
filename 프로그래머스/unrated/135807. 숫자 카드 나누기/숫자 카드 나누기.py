### 문제 이해 ###
# 두 조건 중 하나를 만족하는 가장 큰 양의 정수 a의 값을 구해라.
# 1. 정수 a로 철수가 가진 숫자들은 모두 나눌 수 있고,
#    영희가 가진 숫자들은 모두 나누지 못하는 수.
# 2. 정수 a로 처루가 가진 숫자들은 모두 나눌 수 없고,
#    영희가 가진 카드는 모두 나눌 수 있는 수.
# 만약 두 조건을 달성할 수 있는 수가 없다면 0을 리턴
### 문제 해결 ###
# A의 공약수를 구하고 B의 공약수를 구해 겹치지 않는 수를 리턴

# 최대 공약수를 찾는 함수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(arrayA, arrayB):
    
### 조건 1
    gcd_A = arrayA[0]
    for num in arrayA:
        gcd_A = gcd(gcd_A, num)

    result_A = gcd_A
    for num in arrayB:
        if num % gcd_A == 0:
            result_A = gcd_A // gcd(num, gcd_A)
    
    
### 조건 2
    gcd_B = arrayB[0]
    for num in arrayB:
        gcd_B = gcd(gcd_B, num)

    result_B = gcd_B
    for num in arrayA:
        if num % gcd_B == 0:
            result_B = gcd_B // gcd(num, gcd_B)
        
    if result_A > result_B:
        return result_A
    elif result_A == result_B:
        return 0
    else:
        return result_B