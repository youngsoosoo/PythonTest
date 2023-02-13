import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())

result = []

for i in range(n):
	x = int(input())
	if not x: 
		if len(result) == 0:
			print(0)
		else:
			print(hq.heappop(result)[1])
	else:
		hq.heappush(result, (abs(x), x))