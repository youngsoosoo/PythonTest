arr=[[0 for i in range(100)] for i in range(100)]
n = int(input())
cnt=0
for _ in range(n):
  x, y = map(int, input().split())
  for i in range(x, x+10):
    for j in range(y, y+10):
      arr[i][j] = 1
  
for i in range(100):
  for j in range(100):
    if arr[i][j] == 1:
      cnt+=1
  
    
print(cnt)