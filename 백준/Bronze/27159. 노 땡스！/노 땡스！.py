import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
a=x[0]
for i in range(1, n):
	if x[i]-x[i-1] != 1:
		a+=x[i]
print(a)