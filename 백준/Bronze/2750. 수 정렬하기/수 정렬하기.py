n = int(input())
a=[]
for _ in range(n):
  a.append(int(input()))
a.sort()
for i in range(len(a)):
  print(a[i])