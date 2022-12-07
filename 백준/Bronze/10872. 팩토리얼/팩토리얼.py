import sys
n=int(sys.stdin.readline())
for i in range(1, n):
    n *= i
if n==0:
    print(1)
else:
    print(n)