import sys
input = sys.stdin.readline

# 크루스칼

# 1. 모든 링크를 한 번에 가져온다.
# 2. 링크를 연결하면서 같은 집합으로 만들어준다.
# 3. 만약에 이미 같은 집합이라면 연결하지 않는다.

# union 최적화!
def _find(x):
	while par[x] != x: # 루트가 아니라면
		x = par[x]
	return x
	
def _union(a, b):
	a = _find(a)
	b = _find(b)
	
	if a == b:
		return
	
	if rank[a] < rank[b]:
		par[a] = b
	elif rank[b] < rank[a]:
		par[b] = a
	else:
		par[a] = b
		rank[b] += 1

N, M = map(int, input().split())

link = [list(map(int, input().split())) for _ in range(M)]
link.sort(key = lambda x:x[2]) # 가중치를 기준으로 정렬

par = [i for i in range(1_000_001)]
rank = [0 for _ in range(1_000_001)]

ans = 0

for i in range(M):
	A = link[i][0]
	B = link[i][1]
	weight = link[i][2]
	
	A = _find(A)
	B = _find(B)
	
	if A == B:
		continue
	else:
		_union(A, B)
		ans += weight
print(ans)