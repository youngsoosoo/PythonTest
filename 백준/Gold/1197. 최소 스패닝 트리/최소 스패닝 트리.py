# 프림

import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for i in range(N+1)]

for _ in range(M):
	A, B, C = map(int, input().split())
	graph[A].append([C, B])
	graph[B].append([C, A])
	
# 다익스트라!
q = [[0, 1]] # 1에서 출발할 거다. 가중치 없이
answer = 0
cnt = 0

while q:
	if cnt == N:
		break
		
	weight, node = heapq.heappop(q) # 최소 비용을 꺼내줄겁니다.
	
	# [node, weight] 작은 노드부터 탐색
	if visited[node] == 0:
		answer += weight
		visited[node] = 1
		cnt+=1
		for nxt in graph[node]:
			heapq.heappush(q, nxt)

print(answer)