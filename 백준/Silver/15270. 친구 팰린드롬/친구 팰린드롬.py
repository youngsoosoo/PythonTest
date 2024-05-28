import sys
input = sys.stdin.readline

n, m = map(int, input().split())
fri = [list(map(int, input().split())) for i in range(m)]
answer = 0

def dfs(idx, ans, visited):
	
	global answer
	
	if idx == m:
		answer = max(answer, ans)
		return
	
	if fri[idx][0] in visited or fri[idx][1] in visited:
		dfs(idx+1, ans, visited)
	else:
		dfs(idx+1, ans+1, visited + fri[idx])
		dfs(idx+1, ans, visited)

dfs(0, 0, [])

answer*=2

if answer < n:
	answer+=1

print(answer)