import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
if m:
	channel = list(map(int, input().split()))
else:
	channel = []

cnt = abs(n - 100)

for num in range(1000001):
	num = str(num)
	
	for j in range(len(num)):
		if int(num[j]) in channel:
			break
		elif j == len(num) - 1:
			cnt = min(cnt, abs(int(num) - n) + len(num))


print(cnt)