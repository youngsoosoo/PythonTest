A, B, C = map(int, input().split())

if B < C:
  print(A//(C-B)+1)
else:
  print(-1)