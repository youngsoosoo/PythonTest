import sys
from math import factorial
input = sys.stdin.readline

for i in range(int(input())):
	n, k = map(int, input().split())
	print(factorial(k)//(factorial(n)*factorial(k-n)))