import sys
from itertools import combinations
input = sys.stdin.readline

n, c = map(int, input().split())
w = list(map(int, input().split()))

answer = 1
leftw = w[:n//2]
rightw = w[n//2:]
left = []
right = []

for i in range(1, len(leftw) + 1):
	for j in combinations(leftw, i):
		sumValue = sum(j)
		if sumValue <= c:
			left.append(sumValue)
	
for i in range(1, len(rightw) + 1):
	for j in combinations(rightw, i):
		sumValue = sum(j)
		if sumValue <= c:
			right.append(sumValue)
right.sort()

for i in left:
	start, end = 0, len(right)
	while start < end:
		mid = (start+end) // 2
		if i + right[mid] <= c:
			start = mid + 1
		else:
			end = mid
	answer += end
print(len(left) + len(right) + answer)