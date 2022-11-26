a = int(input())
result = a
count = 0

while True:
  ten = int(a/10)
  one = a%10
  a = ten + one
  a = one*10 + a%10
  count += 1
  if result == a:
    print(count)
    break