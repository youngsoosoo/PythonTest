import sys
input = sys.stdin.readline
	
n, c = map(int, input().split())
x = [int(input()) for i in range(n)]
x.sort()

start, end = 1, x[-1]-x[0]
result=0

while start <= end :
	mid = (start + end) // 2
	cut = x[0]
	cnt=1
	for i in range(1, len(x)):
		if x[i] >= cut + mid:
			cnt += 1
			cut = x[i]
	
	if cnt >= c:
		start = mid + 1
		result = mid
	else:
		end = mid - 1

print(result)