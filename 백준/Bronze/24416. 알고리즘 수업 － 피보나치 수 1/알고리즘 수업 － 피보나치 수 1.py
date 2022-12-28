import sys
input = sys.stdin.readline

n = int(input())

def fibonacci(n):
	for i in range(3, n+1):
		f[i] = f[i-1]+f[i-2]
	return f[n]
f=[1]*(n+1)
print(fibonacci(n), n-2)