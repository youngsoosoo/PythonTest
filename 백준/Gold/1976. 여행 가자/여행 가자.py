import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def _union(A, B):
	A = _find(A)
	B = _find(B)
	
	if A == B:
		return
	
	if rank[A] < rank[B]:
		par[A] = B
	elif rank[A] > rank[B]:
		par[B] = A
	else:
		par[A] = B
		rank[B] += 1

def _find(A):
	
	if par[A] != A:
		par[A] = _find(par[A])
	return par[A]

N = int(input())
M = int(input())
par = [i for i in range(N+1)]
rank = [0 for i in range(N+1)]
for i in range(1, N+1):
	arr = list(map(int, input().split()))
	for j in range(1, N+1):
		if arr[j-1] == 1:
			_union(i, j)

# 여행 경로
path = list(map(int, input().split()))
result = set([_find(i) for i in path])
if len(result) != 1:
	print('NO')
else:
	print('YES')