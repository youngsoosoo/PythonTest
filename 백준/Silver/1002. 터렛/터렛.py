import sys
import math
input = sys.stdin.readline

for _ in range(int(input())) : 
	x1, y1, r1, x2, y2, r2 = map(int, input().split())
	#두 점 사이의 거리
	result = math.sqrt((x1-x2)**2 + (y1-y2)**2)
	
	if result == 0:
		if r1 == r2:
			print(-1)
		else :
			print(0)
	else:
		if result == abs(r1-r2) or result == r1+r2:
			print(1)
		elif result < (r1+r2) and result > abs(r1-r2) :
			print(2)
		else :
			print(0)