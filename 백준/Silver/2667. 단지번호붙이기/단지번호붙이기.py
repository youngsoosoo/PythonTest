import sys
input = sys.stdin.readline

n = int(input())
apt = [input().strip() for i in range(n)]
visited = [[False for i in range(n)] for i in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
	global cnt
	visited[x][y] = True
	if apt[x][y] == '1':
		cnt += 1
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0 <= nx < n and 0 <= ny < n:
			if not visited[nx][ny] and apt[nx][ny]=="1":
				dfs(nx, ny)


result = []
for i in range(n):
	for j in range(n):
		if apt[i][j]=="1" and not visited[i][j]:
			cnt = 0
			dfs(i, j)
			result.append(cnt)

print(len(result))
result.sort()
for i in result:
	print(i)