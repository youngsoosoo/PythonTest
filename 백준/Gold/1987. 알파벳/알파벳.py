import sys
input = sys.stdin.readline


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

r, c = map(int, input().split())
graph = [list(input()) for i in range(r)]
result = set()
answer = 0

def dfs(x, y, cnt):
	global answer
	
	answer = max(answer, cnt)
	result.add(graph[x][y])
	
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in result:
			dfs(nx, ny, cnt + 1)
		
	result.remove(graph[x][y])

dfs(0, 0, 1)

print(answer)