import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	arr = [[0, 0] for i in range(n+1)]
	for _ in range(m):
		a, b, p, q = map(int, input().split())
		
		arr[a][0] += p
		arr[a][1] += q
		arr[b][0] += q
		arr[b][1] += p
	max_value = 0
	min_value = sys.maxsize
	for S, A in arr[1:]:
		s = S**2
		a = A**2
		w=0
		if s+a != 0:
			w = s/(s+a)

		result = math.floor(w*1000)
		max_value = max(max_value, result)
		min_value = min(min_value, result)
	
	print(max_value)
	print(min_value)