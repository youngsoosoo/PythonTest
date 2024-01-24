import sys
input = sys.stdin.readline

def _union(A, B):
	
	A = _find(A)
	B = _find(B)
	
	if A != B:
		par[B] = A
		num[A] += num[B]
	
	print(num[A])
	
	
	
def _find(A):
	
	if A == par[A]:
		return A
	else:
		par[A] = _find(par[A])
		return _find(par[A])


answer = 0

for i in range(int(input())):
	
	F = int(input())
	par, num = {}, {}
	for j in range(F):
		fri1, fri2 = map(str, input().strip().split())
		
		if fri1 not in par:
			par[fri1] = fri1
			num[fri1] = 1
			
		if fri2 not in par:
			par[fri2] = fri2
			num[fri2] = 1
		
		_union(fri1, fri2)