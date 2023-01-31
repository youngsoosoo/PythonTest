import sys
input = sys.stdin.readline

n = int(input())
bd = [input().strip() for i in range(n)]
result=[]
def d(x, y, n):
	
	color = bd[x][y]
	for i in range(x, x+n):
		for j in range(y, y+n):
			if color != bd[i][j]:
				result.append("(")
				d(x, y, n//2)
				d(x, y+n//2, n//2)
				d(x+n//2, y, n//2)
				d(x+n//2, y+n//2, n//2)
				result.append(")")
				return
	if color == 0:
		result.append('0')
	elif color == 1:
		result.append('1')
	else:
		result.append(str(color))


d(0,0,n)
print("".join(result))