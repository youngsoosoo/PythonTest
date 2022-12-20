import sys, math
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
if len(a) < 2:
	print(a[0]**2)
else :
	print(a[0]*a[-1])