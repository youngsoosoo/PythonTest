arr=[[0 for i in range(100)] for i in range(100)]
n = int(input())
cnt=0
for _ in range(n):
  x, y = map(int, input().split())
  for i in range(x, x+10):
    for j in range(y, y+10):
      if arr[i][j] == 0 and i<100 and j<100:
        arr[i][j] += 1
        cnt += 1

print(cnt)