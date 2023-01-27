import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for i in range(n):
	m, k = map(int, input().split())
	li = deque(list(map(int, input().split())))
	cnt = 0
	
	while True:
		if li[0] == max(li):
			li.append(0)
			li.popleft()
			cnt+=1
			if k==0 :
				print(cnt)
				break
		else:
			li.append(li.popleft())
		if k>0:
			k-=1
		else:
			k=m-1