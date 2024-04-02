from collections import deque
def solution(n, edge):
    answer = 0
    
    distance = [-1] * (n+1)
    graph = [[] for i in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque([1])
    distance[1] = 0
    
    while q:
        x = q.popleft()
        
        for i in graph[x]:
            if distance[i] == -1:
                q.append(i)
                distance[i] = distance[x] + 1
    
    max_distance = max(distance)
    for d in distance:
        if d == max_distance:
            answer+=1
    
    return answer