import sys
input = sys.stdin.readline

N, M = map(int ,input().split())
nList = sorted(list(map(int, input().split())))
visited = [False] * N
arr = []
def dfs():
	
	if len(arr) == M:
		print(*arr)
		return
	
	
	number = 0
	for i in range(N):
		if not visited[i] and nList[i] != number:
			visited[i] = True
			arr.append(nList[i])
			number = nList[i]
			dfs()
			visited[i] = False
			arr.pop()
dfs()