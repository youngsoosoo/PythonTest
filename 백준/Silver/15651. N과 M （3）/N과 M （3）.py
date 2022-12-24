import sys
input = sys.stdin.readline

def dfs():
	if len(s) == m:
		print(*s)
		return
	for i in range(1, n+1):
		s.append(i)
		dfs()
		s.pop()

s=list()
n, m = map(int, input().split())

dfs()