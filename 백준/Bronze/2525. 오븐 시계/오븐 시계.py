A, B = input().split()
A = int(A)
B = int(B)
C = int(input())

D = A*60 + B + C
A = int(D/60)
B = D%60

if A>=24 :
  A -= 24

print(A, B)