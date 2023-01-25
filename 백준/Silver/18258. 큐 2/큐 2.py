import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a=deque([])
for i in range(n):
	s = input().strip().split()
	
	if s[0] == 'push':
		a.append(s[1])
		continue
	elif s[0] == 'size':
		print(len(a))
		continue
	else:
		if len(a) > 0:
			if s[0] == 'front':
				print(a[0])
				continue
			elif s[0] == 'back':
				print(a[-1])
				continue
			elif s[0] == 'pop':
				print(a.popleft())
				continue
			elif s[0] == 'empty':
				print("0")
		else:
			if s[0] == 'empty':
				print("1")
				continue
			print("-1")