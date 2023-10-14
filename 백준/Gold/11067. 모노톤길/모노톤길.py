import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	n = int(input())
	graph = [[] for i in range(100001)]
	for _ in range(n):
		x, y = map(int, input().split())
		graph[x].append(y)
	
	result = [[0, 0]]
	for i in range(100001):
		
		if graph[i]:
			graph[i].sort()
			if result[-1][1] <= graph[i][0]:
				for j in graph[i]:
					result.append([i, j])
			else:
				for j in graph[i][::-1]:
					result.append([i, j])
	
	kmap = list(map(int, input().split()))
	for i in kmap[1:]:
		for j in result[i]:
			print(j, end=" ")
		print()