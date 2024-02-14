import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
answer = 0
graph = [[] for i in range(n+1)]
start = -1

for i in range(n-1):
	# 노드, 노드, 가중치
	a, b, c = map(int, input().split())
	graph[a].append([b, c])
	graph[b].append([a, c])

def dfs(node, weight):
	global start, startWeight
	for a, w in graph[node]:
		if dis[a] == -1:
			dis[a] = weight + w
			if startWeight < weight + w:
				start = a
				startWeight = weight + w
			dfs(a, weight + w)

# 루트 노드로 부터 가장 먼 노드까지의 길이 구하기 - A
dis = [-1] * (n+1)
dis[1] = 0
startWeight = 0
dfs(1, 0)
answer += startWeight
# A에서 구한 노드의 가장 먼 노드까지의 길이 구하기 - B
dis = [-1] * (n+1)
dis[start] = 0
startWeight = 0
dfs(start, 0)
# B의 값을 출력
print(startWeight)