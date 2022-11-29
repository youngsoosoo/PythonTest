N = int(input())

count = 0
for _ in range(N):
  word = input()
  a=0
  for i in range(len(word)-1):
    if word[i] != word[i+1]:
      new = word[i+1:]
      if new.count(word[i]) > 0:
        a += 1
  if a == 0:
    count += 1
  
print(count)