import sys
input = sys.stdin.readline

graph = [[] for i in range(9)]
blank = []

for i in range(9):
	graph[i] = list(map(int, input().split()))
	
# 1. 가로에 같은 숫자가 없는지 확인한다.
# 2. 세로에 같은 숫자가 없는지 확인한다.
# 3. 3*3 정사각형 안에도 같은 숫자가 없는지 확인한다.//3 의 몫으로 판단해서 체크해주면 될듯?

# 스도쿠 검증
# 1
def row(i, x):
	if x in graph[i]:
		return False
	return True

# 2
def column(j, x):
	for i in range(9):
		if x == graph[i][j]:
			return False
	return True

# 3
def square(i, j, x):
	for k in range(3):
		if x in graph[i//3 * 3 + k][j//3 * 3 : j//3 * 3 + 3]:
			return False
	return True

def find(n):
	if n == len(blank):
		for i in graph:
			print(*i)
		exit()
	
	for k in range(1, 10):
		i = blank[n][0]
		j = blank[n][1]
		if row(i, k) and column(j, k) and square(i, j, k):
			graph[i][j] = k
			find(n+1)
			graph[i][j] = 0

for i in range(9):
	for j in range(9):
		if graph[i][j] == 0:
			blank.append([i, j])

find(0)