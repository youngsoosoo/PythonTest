import sys
input = sys.stdin.readline
	
n = int(input())
arr = []

for _ in range(n):
	x, y = map(int, input().split())
	arr.append((x, y))
for i in arr:
	cnt = 1
	for j in arr:
		if i[0] < j[0] and i[1] < j[1]:
			cnt+=1
	print(cnt, end=" ")

