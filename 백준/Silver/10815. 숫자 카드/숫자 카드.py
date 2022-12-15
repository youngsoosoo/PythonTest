import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(str, input().split()))
arr = set(arr)
m = int(input())

for i in input().split():
	print(1 if i in arr else 0, end=" ")