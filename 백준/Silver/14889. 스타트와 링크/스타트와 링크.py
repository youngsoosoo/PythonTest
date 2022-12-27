import sys
input = sys.stdin.readline

def dfs(a, idx):
	global result
	if a == n//2:
		lt, st = 0, 0
		for i in range(n):
			for j in range(n):
				if visited[i] and visited[j]:
					lt += arr[i][j]
				elif not visited[i] and not visited[j]:
					st += arr[i][j]
		result= min(result, abs(lt-st))
		return

	for i in range(idx, n):
		if not visited[i]:
			visited[i] = True
			dfs(a+1, i+1)
			visited[i] = False

n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
result=int(1e9)
dfs(0, 0)

print(result)