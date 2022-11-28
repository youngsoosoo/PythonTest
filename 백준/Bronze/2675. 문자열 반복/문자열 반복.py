N=int(input())

for i in range(0,N):
  A, B = input().split()
  A = int(A)
  for k in range(len(B)):
    for j in range(0, A):
      print(B[k], end="")
  print()