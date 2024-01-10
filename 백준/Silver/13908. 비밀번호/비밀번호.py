import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
hint = list(map(int, input().split()))

answer = 0

def dfs(ans):
	global answer
	
	if len(ans) == n:
		for i in hint:
			if i not in ans:
				return
		answer+=1
			
		return
	
	for i in range(10):
		ans.append(i)
		dfs(ans)
		ans.pop()
	
for i in range(10):
	ans = []
	ans.append(i)
	dfs(ans)
	ans.pop()

print(answer)