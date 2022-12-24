import sys
input = sys.stdin.readline
a=1
def dfs(a):
	if len(s) == m:
		print(*s)
		return
	for i in range(a, n+1):
		s.append(i)
		dfs(i)
		s.pop()

s=list()
n, m = map(int, input().split())

dfs(a)