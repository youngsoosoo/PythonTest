import sys
input = sys.stdin.readline

N = int(input())

queen = [0] * N
answer = 0

def vaild(x):
	for i in range(x):
		# 세로 x, 대각선 x
		if queen[x] == queen[i] or abs(queen[x] - queen[i]) == abs(x-i):
			return False
	return True
	
def nqueen(x):
	global answer
	if x == N:
		answer+=1
		return
	else:
		for i in range(N):
			queen[x] = i
			if vaild(x):
				nqueen(x+1)

nqueen(0)
print(answer)	