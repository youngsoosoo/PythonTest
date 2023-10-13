import sys
from fractions import Fraction
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	a, b = map(int,input().split())
	while a!=1:
		x = b//a+1
		a = a*x-b
		b *= x
		a, b = map(int, str(Fraction(a, b)).split('/'))
	print(b)