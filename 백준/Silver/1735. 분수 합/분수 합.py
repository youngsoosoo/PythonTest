import sys
input = sys.stdin.readline

def gcd(x, y):
	
	m = x % y
	while m > 0:
		x = y
		y = m
		m = x % y
	return y
	
a, b = map(int, input().split())
c, d = map(int, input().split())

e, f = a*d + c*b, b*d
answer = gcd(e, f)
print(e // answer, f // answer)