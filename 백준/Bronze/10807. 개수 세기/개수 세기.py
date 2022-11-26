N = int(input())
a = map(int, input().split())
b = int(input())
count = 0
for i in a:
  if i == b:
    count = count + 1
print(count)