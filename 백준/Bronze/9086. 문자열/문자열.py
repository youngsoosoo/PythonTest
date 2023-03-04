import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
	s = input().strip()
	print(s[0], end='')
	print(s[-1])