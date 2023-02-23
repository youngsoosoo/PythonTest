import sys
import heapq as hq
input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
k = int(input())
dp = [INF] * (V+1)
heap=[]
graph = [[] for i in range(V+1)]

def dik(start):
	dp[start] = 0
	hq.heappush(heap, (0, start))
	
	while heap:
		a, b = hq.heappop(heap)
		
		if dp[b] < a:
			continue
			
		for w, n in graph[b]:
			nw = w + a
			if nw < dp[n]:
				dp[n] = nw
				hq.heappush(heap, (nw, n))



for i in range(E):
	u, v, w = map(int, input().split())
	graph[u].append((w, v))

dik(k)

for i in range(1, V+1):
	print("INF" if dp[i] == INF else dp[i])