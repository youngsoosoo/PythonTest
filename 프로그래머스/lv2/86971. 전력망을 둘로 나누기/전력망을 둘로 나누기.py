from collections import deque
def solution(n, wires):
    answer = n
    graph = [[] for i in range(n+1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    #dfs를 통해 먼저 9를 출력해보자
    def bfs(start):
        q = deque([start])
        visited = [0 for i in range(n+1)]
        visited[start] = 1
        cnt = 1
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
                    cnt+=1
        return cnt

    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        answer = min(abs(bfs(v1)-bfs(v2)), answer)
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return answer