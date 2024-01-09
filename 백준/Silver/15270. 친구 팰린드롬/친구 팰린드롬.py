import sys
input = sys.stdin.readline

N, M = map(int, input().split())
fri = [list(map(int, input().split())) for i in range(M)]
answer = 0

def dfs(n, ans, visited):
	
	global answer
	
	if n == M:
		answer = max(answer, ans)
		return
	
	if fri[n][0] in visited or fri[n][1] in visited:
		dfs(n+1, ans, visited)
	else:
		dfs(n+1, ans+1, visited + fri[n])
		dfs(n+1, ans, visited)

dfs(0, 0, [])

answer*=2

if answer < N:
	answer+=1

print(answer)