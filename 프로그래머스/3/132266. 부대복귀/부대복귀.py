from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] for i in range(n+1)]
    desti = [-1 for i in range(n+1)]
    desti[destination] = 0
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque([destination])
    while q:
        x = q.popleft()
        for node in graph[x]:
            if desti[node] == -1:
                desti[node] = desti[x] + 1
                q.append(node)
                
    
    for source in sources:
        answer.append(desti[source])
        
    return answer