import sys
from collections import Counter

n = int(sys.stdin.readline())
a=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

a.sort()

for i in a:
    print(i[0], i[1])