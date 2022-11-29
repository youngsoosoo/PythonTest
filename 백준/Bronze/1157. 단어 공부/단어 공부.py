S = input().upper()
A = [0]*26 #아스키코드 숫자 범위
for i in range(0, len(S)):
  A[ord(S[i])-65] += 1

result = chr(A.index(max(A))+65)

A.sort(reverse=True)
if A[0] == A[1]:
  print("?")
else :
  print(result)