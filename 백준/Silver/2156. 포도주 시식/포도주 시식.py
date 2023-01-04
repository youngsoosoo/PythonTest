import sys
input = sys.stdin.readline
dp=[0]
s=[0]
n = int(input())
for i in range(n):
	s.append(int(input()))

dp.append(s[1])
if n>1:
	dp.append(s[1]+s[2])
for i in range(3, n+1):
	dp.append(max(dp[i - 1], dp[i - 2] + s[i], dp[i - 3] + s[i-1] + s[i]))

print(dp.pop())