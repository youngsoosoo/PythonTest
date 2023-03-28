import sys
from collections import deque
input = sys.stdin.readline


def solutions():
	n, k = map(int, input().split())
	li = [list(map(int, input().split())) for i in range(n)]
	dx = [0, 0, -1, 1]
	dy = [1, -1, 0, 0]
	s, x, y = map(int, input().split())

	q = []


	for j in range(n):
		for k in range(n):
			if li[j][k] != 0:
				q.append((li[j][k], j, k, 0))
	q.sort(key=lambda x:x[0])
	q = deque(q)
	
	while q:
		r, a, b, c = q.popleft()

		if c == s:
			break
		for j in range(4):
			nx = a + dx[j]
			ny = b + dy[j]
			if 0 <= nx < n and 0 <= ny < n and li[nx][ny] == 0:
				li[nx][ny] = li[a][b]
				q.append((li[nx][ny], nx, ny, c+1))

	return li[x-1][y-1]
print(solutions())