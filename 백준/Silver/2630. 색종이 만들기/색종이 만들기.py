import sys
input = sys.stdin.readline

n = int(input())

bd = [list(map(int, input().split())) for _ in range(n)]

result = []

def d(x, y, n):
	color = bd[x][y]
	for i in range(x, x+n):
		for j in range(y, y+n):
			if color != bd[i][j]:
				d(x, y, n//2)
				d(x, y+n//2, n//2)
				d(x+n//2, y, n//2)
				d(x+n//2, y+n//2, n//2)
				return
	if color == 0:
		result.append(0)
	else:
		result.append(1)

d(0,0,n)
print(result.count(0))
print(result.count(1))