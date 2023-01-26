import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
c = deque([])

for i in range(1, n+1):
	c.append(i)
print('<', end='')
while c:
	for i in range(k - 1):
		c.append(c[0])
		c.popleft()
	print(c.popleft(), end='')
	if c:
		print(', ', end='')

print('>')