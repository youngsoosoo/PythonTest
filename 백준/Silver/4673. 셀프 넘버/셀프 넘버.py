def selfnumber(n):
  a = n
  while n != 0:
    a = a + n%10
    n = n//10
  return a

arr = [False] * 10001

for i in range(1, 10001):
  b = selfnumber(i)
  if b<10001:
    arr[b] = True
for i in range(1,len(arr)):
  if arr[i] == False:
    print(i)
