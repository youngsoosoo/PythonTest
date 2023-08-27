import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int ,input().split()))

arr.sort()
for i in permutations(arr, m):
	for j in i:
		print(j, end=" ")
	print()