from collections import deque
import sys

def solution(N, road, K):
    answer = 0
    
    graph = [[] for i in range(N+1)]
    visited = [sys.maxsize for i in range(N+1)]
    visited[1] = 0
    
    for i in road:
        graph[i[0]].append([i[1], i[2]])
        graph[i[1]].append([i[0], i[2]])

    q = deque([(1, 0)])
    
    while q:
        end, dik = q.popleft()

        for b, c in graph[end]:
            if dik + c <= K and dik + c < visited[b]:

                q.append((b, dik + c))
                visited[b] = dik + c
        
        
    for k in visited:
        if k != sys.maxsize:
            answer += 1
    return answer