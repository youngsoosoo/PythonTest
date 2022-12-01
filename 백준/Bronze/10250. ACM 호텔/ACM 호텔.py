t = int(input())

for _ in range(t):
  h, w, n = map(int, input().split())
  a = n%h #n번째손님/층수
  b = n//h+1 #나머지 방
  if n % h == 0:
    b = n//h
    a = h
  print(a*100+b)