t = int(input())



for _ in range(t):
  k = int(input())#k층
  n = int(input())#n호
  f0 = [a for a in range(1, n+1)]
  for i in range(k):
    for j in range(1, n):
      f0[j] += f0[j-1]
  print(f0[-1])
