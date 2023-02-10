import sys
import heapq as hq
input = sys.stdin.readline
	
n = int(input())
x=[]

for _ in range(n):
	i = int(input())
	if i:
		hq.heappush(x, (-i, i))
	else:
		if len(x) >= 1:
			print(hq.heappop(x)[1])
		else:
			print(0)