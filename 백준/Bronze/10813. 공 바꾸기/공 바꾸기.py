import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [i+1 for i in range(n)]

for _ in range(m):
	i, j = map(int, input().split())
	i-=1
	j-=1
	temp = graph[i]
	graph[i] = graph[j]
	graph[j] = temp

print(*graph)
	