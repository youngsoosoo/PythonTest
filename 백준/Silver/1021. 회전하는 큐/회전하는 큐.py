import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
dq = deque([])
cnt=0
for i in range(n):
	dq.append(i+1)
for i in li:
	while True:
		if dq[0] == i:
			dq.popleft()
			break
		if dq.index(i) <= len(dq)//2:
			dq.append(dq.popleft())
			cnt+=1
		else:
			dq.appendleft(dq.pop())
			cnt+=1
print(cnt)