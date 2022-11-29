S = list(map(str, input().split()))
A = S[0]
B = S[1]
if A[::-1] > B[::-1]:
  print(A[::-1])
else :
  print(B[::-1])