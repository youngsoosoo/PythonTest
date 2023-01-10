import sys
input = sys.stdin.readline

s = input()
q = int(input())

for i in range(q):
	a, l, r = input().split()
	l = int(l)
	r = int(r)
	sc = s[l:r+1]
	print(sc.count(a))