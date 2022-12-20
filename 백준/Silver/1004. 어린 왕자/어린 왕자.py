import sys, math
input = sys.stdin.readline


for _ in range(int(input())):
	x1, y1, x2, y2 = map(int, input().split())
	arr = []
	cnt=0
	for qq in range(int(input())):
		cx, cy, r = map(int, input().split())
		d1 = math.sqrt((x1-cx)**2 + (y1-cy)**2) #출발점
		d2 = math.sqrt((x2-cx)**2 + (y2-cy)**2) #도착점
		if r > d1 and r > d2 :
			pass
		elif r > d1 or r > d2 :
			cnt += 1
	print(cnt)