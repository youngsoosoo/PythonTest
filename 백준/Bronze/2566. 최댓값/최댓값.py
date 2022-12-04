a=[[i for i in map(int, input().split())] for i in range(9)]

print(max(map(max,a)))

for i in range(9):
  for j in range(9):
    if a[i][j] == max(map(max,a)):
      print(i+1, j+1)