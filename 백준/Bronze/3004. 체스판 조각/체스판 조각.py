import sys
input = sys.stdin.readline
n = int(input())

if n%2==0:
	a = (n//2)+1
	print(a*a)
else :
	a = (n//2)+1
	print(a*(a+1))