A=int(input())

for _ in range(A):
  B = list(map(int, input().split()))
  count = 0
  avr = sum(B[1:]) / B[0]
  for i in B[1:]:
    if i>int(avr):
      count += 1
  pre = count/(len(B)-1)*100
  print(f'{pre:.3f}%')