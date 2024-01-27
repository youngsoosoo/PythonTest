import sys
input = sys.stdin.readline

def _find(A):
	
	if par[A] != A:
		return _find(par[A])
	return par[A]

def _union(A, B):
	A = _find(A)
	B = _find(B)
	
	if A == B:
		return
	
	if rank[A] > rank[B]:
		par[B] = A
	elif rank[A] < rank[B]:
		par[A] = B
	else:
		par[B] = A
		rank[A] += 1
		
def dif(A, B):
	return ((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2) ** 0.5
		
N, M = map(int, input().split())

par = [i for i in range(N+1)]
rank = [0 for i in range(N+1)]

stars = []
edges = []

answer = 0

for _ in range(N):
	X, Y = map(int, input().split())
	stars.append((X, Y))
	
for _ in range(M):
	X, Y = map(int, input().split())
	_union(X-1, Y-1)
	
for i in range(N-1):
	for j in range(i+1, N):
		edges.append((dif(stars[i], stars[j]), i, j))
		
edges.sort(key=lambda x : x[0])

for cost, x, y in edges:
	if _find(x) != _find(y):
		_union(x, y)
		answer+=cost
		
print("{:.2f}".format(answer))