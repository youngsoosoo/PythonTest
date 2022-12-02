n = int(input())
arr = list(map(int, input().split()))
def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False # i로 나누어 떨어지면 소수가 아니므로 False 리턴
    
    return True # False가 리턴되지 않고 for문을 빠져나왔다면 소수이므로 True 리턴

cnt=0
for _ in arr:
  if isprime(_):
    cnt += 1
  if _ == 1:
    cnt -= 1
  
print(cnt)