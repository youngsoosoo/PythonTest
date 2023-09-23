import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
forest = [list(map(int, input().split())) for i in range(n)]

dp = [[0 for i in range(n)] for j in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def recur(x, y):

	if dp[x][y] != 0:
		return dp[x][y]
	
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if 0 <= ny < n and 0 <= nx < n:
			if forest[x][y] < forest[nx][ny]:
				dp[x][y] = max(dp[x][y], recur(nx, ny) + 1)

	return dp[x][y]
	
for x in range(n):
	for y in range(n):
		recur(x, y)
print(max(map(max, dp)) + 1)