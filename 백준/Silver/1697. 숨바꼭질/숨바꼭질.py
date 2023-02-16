import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

q=deque([n])
visited = [0 for i in range(10**5 + 1)]

while q:
	x = q.popleft()
	if x == k:
		print(visited[x])
		break
	for nx in (x-1, x+1, x*2):
		if 0 <= nx <= 10**5 and not visited[nx]:
			visited[nx] = visited[x] + 1
			q.append(nx)