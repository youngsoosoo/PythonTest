import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
s = int(input())-1

answer = 1
visited = [0] * n
visited[s] = 1

q = deque([s])

while q:
	x = q.popleft()
	for dx in [-a[x], a[x]]:
		nx = x + dx
		
		if 0 <= nx < n and not visited[nx]:
			answer+=1
			q.append(nx)
			visited[nx] = 1

print(answer)