A=int(input())

for i in range(A):
  B= list(input())
  sum = 0
  score=0
  for j in B:
    if j == 'O':
      score += 1
      sum += score
    else :
      score = 0
  print(sum)