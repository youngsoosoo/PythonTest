N = int(input())
i=0
max =0

a = 0 
b = 0 
while N>max:
  i += 1
  max += i
  
A = max - N
if i%2==0:
  a = i - A
  b = A + 1
else:
  a = A+1
  b = i-A

print(f'{a}/{b}')