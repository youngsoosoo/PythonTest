N = int(input())
count = 99

if N<100:
  print(N)
else:
  for i in range(100, N+1):
    one = i%10
    ten = (i//10)%10
    hun = i//100
    if ten-one == hun-ten:
      count += 1
    elif one-ten == ten-hun:
      count += 1
  print(count)
