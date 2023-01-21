import sys
input = sys.stdin.readline

n = int(input())
a=[]

for i in range(n):
	b = list(input().strip().split())
	if b[0] == 'push':
		a.append(b[1])
	elif b[0] == 'pop':
		if len(a) > 0:
			print(a.pop())
		else:
			print(-1)
	elif b[0] == 'size':
		print(len(a))
	elif b[0] == 'empty':
		if len(a) == 0:
			print(1)
		else:
			print(0)
	elif b[0] == 'top':
		if len(a) >0:
			print(a[-1])
		else:
			print(-1)