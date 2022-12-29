import sys
input = sys.stdin.readline

t = int(input())
arr = [1]*101
for _ in range(t):
	n = int(input())
	for i in range(4, n+1):
		arr[i] = arr[i-2]+arr[i-3]
	print(arr[n])