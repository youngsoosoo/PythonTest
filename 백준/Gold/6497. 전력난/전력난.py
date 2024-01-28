import sys
input = sys.stdin.readline

def _find(A):
	
	if A != par[A]:
		par[A] = _find(par[A])
	return par[A]

def _union(A, B):
	
	A = _find(A)
	B = _find(B)

	if A < B:
		par[B] = A
	else:
		par[A] = B

while True:
	# n은 집의 수, m은 길의 수
	n, m = map(int, input().split())
	
	if n == 0 and m == 0:
		break
		
	par = [i for i in range(n)]
	answer = 0
	home = []	
	
	for _ in range(m):
		x, y, cost = map(int ,input().split())
		home.append((x, y, cost))
	home.sort(key=lambda x: x[2])
	
	for x, y, cost in home:

		if _find(x) != _find(y):
			_union(x, y)
		else:
			answer += cost
	print(answer)