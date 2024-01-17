import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def _find(A):
	
	if A == par[A]:
		return A
	else:
		par[A] = _find(par[A])
		return _find(par[A])
	
def _union(A, B):
	A = _find(A)
	B = _find(B)
	
	if A == B:
		return
	
	if rank[A] < rank[B]:
		par[A] = B
	elif rank[B] < rank[A]:
		par[B] = A
	else:
		par[B] = A
		rank[A] += 1

n, m = map(int, input().split())
par = [i for i in range(n)]
rank = [0 for i in range(n)]
answer = 0
for i in range(m):
	a, b = map(int, input().split())
	if _find(a) == _find(b):
		answer = i+1
		break
	
	_union(a, b)
print(answer)