import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

m = int(input())
list_c = list(map(int, input().split()))

q = deque()

for i in range(n):
	if list_a[i] == 0:
		q.appendleft(list_b[i])
		
for i in range(m):
	q.append(list_c[i])
	print(q.popleft(), end=' ')