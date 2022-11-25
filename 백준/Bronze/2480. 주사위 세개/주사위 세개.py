A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

if A == B == C:
  print(10000 + A * 1000)
elif A==B or B==C :
  print(1000 + B * 100)
elif A==C:
  print(1000 + A * 100)
else :
  print(max(A,B,C)*100)