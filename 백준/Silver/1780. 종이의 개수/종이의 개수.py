import sys
input = sys.stdin.readline

n = int(input())
bd = [list(input().strip().split()) for i in range(n)]
result=[]
def d(x, y, n):
	color = bd[x][y].strip()
	for i in range(x, x+n):
		for j in range(y, y+n):
			if color != bd[i][j].strip():
				n = n // 3
				d(x, y, n)					#0,0
				d(x, y+n, n)				#0,3
				d(x+n, y, n)				#3,0
				d(x+n, y+n, n)			#3,3
				d(x+n*2, y, n)		#6,0
				d(x+n*2, y+n, n)	#6,3
				d(x, y+n*2, n)		#0,6
				d(x+n, y+n*2, n)	#3,6
				d(x+n*2, y+n*2, n)#6,6
				return
	if color == '0':
		result.append(0)
	elif color == '1':
		result.append(1)
	else:
		result.append(-1)


d(0,0,n)
print(result.count(-1))
print(result.count(0))
print(result.count(1))