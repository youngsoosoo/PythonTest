import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
_xList = sorted(list(map(int, input().split())))
animals = [list(map(int, input().split())) for i in range(n)]

answer = 0

for x, y in animals:
	start, end = 0, len(_xList)-1
	
	while start <= end:
		mid = (start + end) // 2
		t = l-y
		if _xList[mid] < x - t:
			start = mid + 1
		elif _xList[mid] > x + t:
			end = mid - 1
		else:
			answer+=1
			break

print(answer)