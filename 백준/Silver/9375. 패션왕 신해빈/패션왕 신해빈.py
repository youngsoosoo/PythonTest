import sys
from math import factorial
input = sys.stdin.readline

for _ in range(int(input())):
	a = dict()
	cnt = 1
	for i in range(int(input())):
		arr = list(input().split())
		if arr[1] in a:
			a[arr[1]].append(arr[0])
		else:
			a[arr[1]] = [arr[0]]
	
	for i in a:
		cnt *= (len(a[i])+1)
	print(cnt-1)