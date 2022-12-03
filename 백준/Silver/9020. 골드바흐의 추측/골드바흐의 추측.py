def isPrime(a):
  if a<2:
    return False
  for i in range(2, int(a**0.5)+1):
    if a%i == 0:
      return False
  return True

t = int(input())
for _ in range(0,t):
  n = int(input())
  a=[]
  arr=[]
  if isPrime(n//2):
    print(n//2, n//2)
  else :
    for i in range(2, n):
      if isPrime(i):
        a.append(i)
    for i in a:
      if isPrime(n-i) and n-2*i>0:
        arr.append(n-2*i)
    if len(arr)>0:
      c = (n-min(arr))//2
      print(c, n-c)