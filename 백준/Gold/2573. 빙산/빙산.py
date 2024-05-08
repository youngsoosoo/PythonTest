import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]

answer = 0
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dfs():
	global graph
	visited = [[0 for i in range(m)] for i in range(n)]
	
	for i in range(n):
		for j in range(m):
			if graph[i][j]:
				
				cnt = 0
				visited[i][j] = 1
				for dx, dy in d:
					nx = i + dx
					ny = j + dy
					
					if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and not visited[nx][ny]:
						cnt += 1
				
				graph[i][j] -= cnt
				if graph[i][j] < 0:
					graph[i][j] = 0
	
def _check():
	result = 0
	visited = [[0 for i in range(m)] for i in range(n)]
	
	for i in range(n):
		for j in range(m):
			
			if graph[i][j] and not visited[i][j]:
				result += 1
				q = deque([[i, j]])
				visited[i][j] = 1
				
				while q:
					x, y = q.popleft()
					for dx, dy in d:
						nx = x + dx
						ny = y + dy
					
						if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny]:
							q.append([nx, ny])
							visited[nx][ny] = 1
	
	return result

while True:
	flag = _check()
	if flag == 0:
		answer = 0
		break
	elif flag >= 2:
		break
	dfs()
	answer+=1
	
print(answer)