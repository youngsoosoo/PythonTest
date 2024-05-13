import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

def dfs():
	
	visited = [1] + [0 for i in range(n-1)]
	q = deque([0])
	
	while q:
		node = q.popleft()

		for next_node in range(node+1, n):
			if (next_node-node) * (1 + abs(a[node] - a[next_node])) <= k and not visited[next_node]:
				visited[next_node] = 1
				q.append(next_node)
				if next_node == n-1:
					return 'YES'
	return 'NO'

print(dfs())