import sys
n=int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(sys.stdin.readline().split())
a.sort(key=lambda x : int(x[0]))
for i in range(n):
    print(a[i][0], a[i][1])