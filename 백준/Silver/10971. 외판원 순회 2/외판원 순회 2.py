import sys
input = sys.stdin.readline

N = int(input())
ans = sys.maxsize
W = [list(map(int, input().split())) for i in range(N)]
visited = [0 for i in range(N)]

# 도시 방문 (처음 번호, 현재 번호, 비용, 방문 횟수)
def dfs(n, i, exp, cnt):
	global ans
	
	if cnt == N :
		if W[i][n]:
			exp += W[i][n]
			ans = min(ans, exp)
		return
	
	if exp > ans:
		return
	
	for j in range(N):
		if not visited[j] and W[i][j]:
			visited[j] = 1
			dfs(n, j, exp + W[i][j], cnt+1)
			visited[j] = 0
	

for i in range(N):
	visited[i] = 1
	dfs(i, i, 0, 1)
	visited[i] = 0
print(ans)