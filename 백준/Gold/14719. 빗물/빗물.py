import sys
input = sys.stdin.readline

H, W = map(int, input().split())
graph = list(map(int, input().split()))

answer = 0

for i in range(1, W-1):
	
	left = max(graph[:i])
	right = max(graph[i+1:])
	
	wall = min(left, right)
	
	if graph[i] < wall:
		answer += wall - graph[i]

print(answer)