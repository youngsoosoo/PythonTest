import sys
input = sys.stdin.readline

def chess(color):
	a = [[0] *(m+1) for i in range(n+1)]
	for i in range(n):
		for j in range(m):
			if (i+j) % 2 == 0:
				val=board[i][j]!=color
			else:
				val=board[i][j]==color
			a[i+1][j+1] = a[i][j+1] + a[i+1][j] - a[i][j] + val
	count = 1e9
	for i in range(1, n-k+2):
		for j in range(1, m-k+2):
			count = min(count, a[i+k-1][j+k-1] - a[i+k-1][j-1] - a[i-1][j+k-1] + a[i-1][j-1])
	return count

n, m, k = map(int, input().split())
board = [input().strip() for i in range(n)]

print(min(chess('W'), chess('B')))