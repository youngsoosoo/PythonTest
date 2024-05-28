import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, max(arr) * m
answer = 0

while start <= end:
	mid = (start + end) // 2
	
	if sum([mid//i for i in arr]) >= m:
		answer = mid
		end = mid - 1
	else:
		start = mid + 1

print(answer)