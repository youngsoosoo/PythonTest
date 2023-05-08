import sys
input = sys.stdin.readline

def fac(n):
	global a
	if n != 0:
		a*=n
		n-=1
		fac(n)
	return a
a=1
print(fac(int(input())))