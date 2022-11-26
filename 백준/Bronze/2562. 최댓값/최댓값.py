B =[]

for i in range(0,9):
  B.append(int(input()))
for i in range(0, len(B)):
  if B[i] == max(B):
    print(B[i])
    print(i+1)