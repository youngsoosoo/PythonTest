import sys
input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))

dp = [0 for i in range(n+1)]
for i in range(1, n+1):
	_max = 0
	_min = 10001
	for j in range(i, 0, -1):
		_max = max(_max, score[j-1])
		_min = min(_min, score[j-1])
		dp[i] = max(dp[i], dp[j-1] + (_max - _min))

print(dp[n])