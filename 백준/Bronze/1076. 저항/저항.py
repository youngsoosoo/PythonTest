A = input()
B = input()
C = input()
D = 0
arr = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

for i in range(0,10):
  if arr[i] == A:
    D+=i*10
for i in range(0,10):
  if arr[i] == B:
    D+=i
for i in range(0,10):
  if arr[i] == C:
    while i != 0:
      D = D*10
      i -= 1
    
print(D)