import math
def isPrime(a):
  if a > 1:
    for i in range(2, int(math.sqrt(a))+1):
      if a%i == 0:
        return False
    return True

while True:
  n = int(input())
  cnt = 0
  if n != 0:
    for i in range(n+1, 2*n +1):
      result = isPrime(i)
      if result == True:
        cnt += 1
    print(cnt)
  else : 
    break