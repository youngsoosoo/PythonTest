import math, sys
input = sys.stdin.readline
 
n = int(input())
dp = [0,1]
 
for i in range(2, n+1):
	value = sys.maxsize
	for j in range(1, int(math.sqrt(i)) + 1):
		value = min(value, dp[i - j**2])
	dp.append(value + 1)
	
print(dp[n])