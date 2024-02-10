import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()

while True:
	n = int(input())
	if n == -1:
		break
	if n != 0 and len(q) < N:
		q.append(n)
	elif n == 0:
		q.popleft()
if q:
	print(*q)
else:
	print("empty")