import sys
input = sys.stdin.readline
	
n, m = map(int,input().split())
cm = list(map(int, input().split()))
start, end = 1, max(cm)

while start <= end :
	mid = (start + end) // 2
	lines = 0
	
	for i in cm:
		if i > mid:
			lines += i - mid
	
	if lines >= m:
		start = mid + 1
	else:
		end = mid - 1

print(end)