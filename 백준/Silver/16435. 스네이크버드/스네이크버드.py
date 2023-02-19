


import sys
input = sys.stdin.readline

N, L = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

for fruit in h:
	if fruit > L:
		break
	elif fruit <= L:
		L += 1

print(L)