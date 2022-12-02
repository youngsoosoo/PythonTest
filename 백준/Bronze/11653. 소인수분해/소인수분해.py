n = int(input())
arr=[]
a=2
while a<=n :
  if n>1:
    if n%a==0:
      arr.append(a)
      n /= a
    else:
      a+=1
arr.sort()
for i in arr:
  print(i)