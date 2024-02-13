import sys
input = sys.stdin.readline
from itertools import combinations

n, m, k = map(int,input().split())

ans = 0
result = [*combinations([i for i in range(n)], m)]

for i in result:
	cnt = 0
	for j in range(m):
		if i[j] < m:
			cnt+=1
	if cnt >= k:
		ans += 1

print(ans / len(result))