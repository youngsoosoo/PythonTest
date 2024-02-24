import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 1 <= n <= 10**6
n = int(input())
dp = [[0, []] for _ in range(n + 1)]
dp[1] = [0, [1]]

for x in range(2, n+1):
	
	dp[x] = [dp[x-1][0] + 1, dp[x-1][1] + [x]]
	
	if x%3 == 0 and dp[x//3][0] + 1 < dp[x][0]:
		dp[x] = [dp[x//3][0] + 1, dp[x//3][1] + [x]]
	if x%2 == 0 and dp[x//2][0] + 1 < dp[x][0]:
		dp[x] = [dp[x//2][0] + 1, dp[x//2][1] + [x]]


print(dp[n][0])
print(*reversed(dp[n][1]))