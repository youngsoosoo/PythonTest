import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

S = str(input()).rstrip()
T = str(input()).rstrip()

def dfs(t):
	global answer
	
	if len(t) == len(S):
		if t == S:
			print(1)
			exit()
		return
	
	if len(t) == 0:
		return
	
	
	if t[-1] == 'A':
		dfs(t[:-1])
	if t[0] == 'B':
		dfs(t[1:][::-1])
dfs(T)
print(0)