import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def _union(A, B): # 최대 높이를 확인해서 합쳐준다! 효과적으로!
	A = _find(A)
	B = _find(B)
	
	if A == B:
		return
	
	if rank[A] < rank[B]:
		visited[A] = B
	elif rank[B] < rank[A]:
		visited[B] = A
	else:
		visited[A] = B
		rank[B] += 1

def _find(A): # 만약에 스스로를 부모로 칭하고 있다면
	if visited[A] == A:
		return A
	else:
		visited[A] = _find(visited[A])
		return _find(visited[A])

N, M = map(int, input().split())
visited = [i for i in range(N+1)]
rank = [0 for i in range(N+1)] # 노드, 

for _ in range(M):
	X, A, B = map(int, input().split())
	
	if X == 0:
		_union(A, B)
	else:
		if _find(A) == _find(B):
			print("YES")
		else:
			print("NO")