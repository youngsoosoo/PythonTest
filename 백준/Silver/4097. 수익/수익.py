import sys
input = sys.stdin.readline

while True:
	n = int(input())
	
	if not n:
		break
	
	dp = []
	for _ in range(n):
		p = int(input())
		dp.append(p)
	
	for i in range(1, n):
		dp[i] = max(dp[i-1] + dp[i], dp[i])
	
	print(max(dp))