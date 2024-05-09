import sys
input = sys.stdin.readline

k = int(input())

def recur(n):
	if n == 0:
		return False
	elif n%2:
		return not recur(n//2)
	else:
		return recur(n//2)

print(1 if recur(k-1) else 0)