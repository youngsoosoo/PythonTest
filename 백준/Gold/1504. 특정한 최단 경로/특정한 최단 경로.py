import sys
import heapq as hq
input = sys.stdin.readline
inf = sys.maxsize

n, e= map(int, input().split())
graph=[[] for i in range(n+1)]


for i in range(e):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))
	graph[b].append((a, c))

u, v = map(int, input().split())

def dik(start):
	heap=[]
	dp = [inf for i in range(n+1)]
	dp[start] = 0
	hq.heappush(heap, (0, start))
	
	while heap:
		wei, now_node = hq.heappop(heap)
		
		if dp[now_node] < wei:
			continue
		
		for next_node, w in graph[now_node]:#w는 가중치
			new_wei = w + wei
			if dp[next_node] > new_wei:
				dp[next_node] = new_wei
				hq.heappush(heap, (new_wei, next_node))

	return dp

one = dik(1)
v1 = dik(u)
v2 = dik(v)

result = min(one[u] + v1[v] + v2[n], one[v] + v2[u] + v1[n])

print(result if result < inf else -1)