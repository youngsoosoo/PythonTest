import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

visited = [0 for i in range(10**5 + 1)]
visited[n] = 1
q = deque([n])

while q:
	x = q.popleft()

	if x == k:
		print(visited[x]-1)
		break
		
	for i in (x-1, x+1, x*2):
		if 0 <= i <= 10**5 and not visited[i]:
			if i == x*2:
				visited[i] = visited[x]
				q.appendleft(i)
			else:
				visited[i] = visited[x] + 1
				q.append(i)