def isPrime(a):
  if a<2:
    return False
  for i in range(2, int(a**0.5)+1):
    if a%i == 0:
      return False
  return True

t = int(input())
for _ in range(t):
  n = int(input())
  b, c = n//2, n//2
  while b>0:
    if isPrime(b) and isPrime(c):
      print(b, c)
      break
    else:
      b -= 1
      c += 1