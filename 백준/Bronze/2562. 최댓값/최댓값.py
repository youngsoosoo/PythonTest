B =[]

for i in range(0,9):
  B.append(int(input()))
print(max(B))
print(B.index(max(B))+1)
