import sys
input = sys.stdin.readline

n = int(input())

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

par = [i for i in range(n+1)]
rank = [0 for i in range(n+1)]
stars = []
edges = []
answer = 0

for _ in range(n) :
	x, y = map(float, input().split())
	stars.append((x, y))
	
for i in range(n-1):
	for j in range(i + 1, n):
		edges.append((((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)**0.5, i, j))

for cost, x, y in sorted(edges):
	if _find(x) != _find(y):
		_union(x, y)
		answer += cost
		
print(round(answer, 2))