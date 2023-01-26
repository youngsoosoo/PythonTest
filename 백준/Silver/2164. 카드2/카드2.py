import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
c = deque([])
for i in range(1, n+1):
	c.append(i)
while len(c) > 1:
	c.popleft()
	c.append(c.popleft())
print(c[0])