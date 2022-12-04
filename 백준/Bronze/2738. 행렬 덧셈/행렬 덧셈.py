n, m= map(int,input().split())

a=[[i for i in map(int, input().split())] for i in range(n)]
b=[[i for i in map(int, input().split())] for i in range(n)]

for i in range(n):
  for j in range(m):
    print(a[i][j]+b[i][j], end=" ")
  print()