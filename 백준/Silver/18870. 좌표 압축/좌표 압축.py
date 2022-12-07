import sys
n=int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = sorted(list(set(a)))
dic = {b[i] : i for i in range(len(b))}
for i in a:
    print(dic[i], end=" ")