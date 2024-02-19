import sys
input = sys.stdin.readline

n = int(input())
arr = dict()
for _ in range(n):
	a, b = map(str, input().split())
	if b == "enter":
		arr[a] = b
	else:
		del arr[a]

for i in sorted(arr.keys(), reverse=True):
	print(i)
