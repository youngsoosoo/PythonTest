import sys
input = sys.stdin.readline

n, k = map(int, input().split())
p = 1000000007
def fac(n):
	result =1
	for i in range(2, n+1):
		result = result * i % p
	return result

def dfs(n, p, m):
	if p == 1:
		return n%m
	
	if p%2 == 0:
		return (dfs(n, p//2, m) ** 2) % m
	else:
		return ((dfs(n, p//2, m) ** 2)*n) % m

print(fac(n)*dfs((fac(k) * fac(n-k)), p-2, p)%p)