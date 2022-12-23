import sys
from math import factorial
input = sys.stdin.readline

def cnt(a,b) :
	result = 0
	while a != 0:
		a = a//b
		result+=a
	return result

n, m = map(int, input().split())

two = cnt(n, 2) - cnt(m, 2) - cnt(n-m, 2)
five = cnt(n, 5) - cnt(m, 5) - cnt(n-m, 5)

print(min(two, five))
