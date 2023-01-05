import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dpr = [0 for _ in range(n)]


for i in range(n):
	for j in range(i):
		if a[i] > a[j] and dp[i] < dp[j] :
			dp[i] = dp[j]
	dp[i] +=1

for i in range(n-1, -1, -1):
	for j in range(n-1, i, -1):
		if a[i] > a[j] and dpr[i] < dpr[j] :
			dpr[i] = dpr[j]
	dpr[i] +=1
a=0
for i in range(n):
	a=max(a, dp[i] + dpr[i] - 1)
print(a)
