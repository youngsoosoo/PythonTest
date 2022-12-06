import sys
a=[]
n = int(sys.stdin.readline())

for i in range(n):
  a.append(sys.stdin.readline().strip())
a = list(set(a))
a.sort()
a.sort(key=len)


for i in a:
    print(i)