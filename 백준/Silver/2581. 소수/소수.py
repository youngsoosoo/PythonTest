m = int(input())
n = int(input())

arr=[]
for num in range(m, n+1):
  error = 0
  if num>1:
    for i in range(2, num):
      if num%i==0:
        error+=1
    if error ==0:
      arr.append(num)
        
if len(arr) == 0:
  print(-1)
else :
  print(sum(arr))
  print(min(arr))