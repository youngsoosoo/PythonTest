import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [1 for i in range(n)]

for i in range(1, n):
	for j in range(i):
		if a[i] > a[j]:
			dp[i] = max(dp[i], dp[j]+1)

len_result = max(dp)
print(len_result)
result = []

for i in range(n-1, -1, -1):
	if dp[i] == len_result:
		result.append(a[i])
		len_result -= 1
		

print(*result[::-1])