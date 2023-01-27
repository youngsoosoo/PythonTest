import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a=deque([])
for i in range(n):
	s = list(input().strip().split())
	
	if s[0] == 'push_front':
		a.appendleft(s[1])
	elif s[0] == 'push_back':
		a.append(s[1])
	elif s[0] == 'pop_front':
		if len(a) == 0:
			print(-1)
			continue
		print(a.popleft())
	elif s[0] == 'pop_back':
		if len(a) == 0:
			print(-1)
			continue
		print(a.pop())
	elif s[0] == 'size':
		print(len(a))
	elif s[0] == 'empty':
		if len(a) == 0:
			print(1)
		else:
			print(0)
	elif s[0] == 'front':
		if len(a) == 0:
			print(-1)
			continue
		print(a[0])
	elif s[0] == 'back':
		if len(a) == 0:
			print(-1)
			continue
		print(a[-1])