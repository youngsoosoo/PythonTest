import sys
input = sys.stdin.readline

while True:
	n = int(input())
	
	if not n:
		break
	
	dp = []
	for i in range(n):
		dp.append(int(input()))
		if i > 0:
			dp[i] = max(dp[i-1] + dp[i], dp[i])
	
	print(max(dp))