import sys
input = sys.stdin.readline

n = int(input())
s = [tuple(map(int, input().split())) for _ in range(n)]
s.sort(key=lambda x : x[0])
dp=[0 for i in range(n)]

for i in range(n):
	for j in range(i):
		if s[i][1] > s[j][1] and dp[i] < dp[j]:
			dp[i] = dp[j]
	dp[i] += 1
print(n-max(dp))