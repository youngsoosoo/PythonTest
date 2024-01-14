import sys
input = sys.stdin.readline

N = int(input())

# 좋은 수열을 판별하는 함수
def check(n, value):
	
	for i in range(1, n//2 + 1):
		if value[-i:] == value[-(i*2):-i]:
			return False
	return True

# 재귀 함수(1 or 2 or 3)
def dfs(n, value):
	
	if n == N:
		print(value)
		exit()
	
	for i in [1, 2, 3]:
		if check(n+1, str(value*10 + i)):
			dfs(n+1, value*10 + i)

dfs(0, 0)