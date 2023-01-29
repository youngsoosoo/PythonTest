import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	p = input().strip()
	n = int(input())
	x = deque(input().rstrip()[1:-1].split(","))
	
	if n == 0:
		x = deque()
	re = 0
	rev = 0
	for i in range(len(p)):
		if p[i] == 'R':
			rev += 1
		elif p[i] == 'D':
			if len(x) == 0:
				print("error")
				re = 1
				break
			else:
				if rev % 2 == 0:
					x.popleft()
				else:
					x.pop()
	if re == 0:
		if rev % 2 == 0:
			print("["+",".join(x)+"]")
		else:
			x.reverse()
			print("["+",".join(x)+"]")