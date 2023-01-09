import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nrr = list(map(int, input().split()))
arr=[0]

a=0
for i in nrr:
	a+=i
	arr.append(a)
for _ in range(m):
	i, j = map(int, input().split())
	print(arr[j]-arr[i-1])