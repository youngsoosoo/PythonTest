X = int(input())
N = int(input())
c=0
for i in range(0, N) :
  a, b = input().split()
  a = int(a)
  b = int(b)
  c += a*b
if(X == c):
  print("Yes")
else:
  print("No")