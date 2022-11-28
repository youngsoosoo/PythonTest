S = input()

arr=[-1] * 26
for i in range(0, len(S)):
  for j in range(0, 26):
    if arr[j] == -1:
      if S[i] == chr(j+97):
        arr[j] = i

for i in range(0, 26):
  print(arr[i], end=' ')