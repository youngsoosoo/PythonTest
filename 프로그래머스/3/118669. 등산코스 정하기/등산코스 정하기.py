from heapq import heappush, heappop
def solution(n, paths, gates, summits):
    # [산봉우리의 번호, intensity의 최솟값]
    answer = [0, 10000001]
    
    summits.sort()
    summits_set = set(summits)
    
    graph = [[] for i in range(n+1)]
    for a, b, m in paths:
        graph[a].append((b, m))
        graph[b].append((a, m))
    
    visited = [10000001] * (n+1)
    q = []
    
    for gate in gates:
        heappush(q, (gate, 0))
        visited[gate] = 0
        
    while q:
        node, weight = heappop(q)
            
        if node in summits_set or weight > visited[node]:
            continue
                
        for n, w in graph[node]:
            intensity = max(weight, w)
            if intensity < visited[n]:
                visited[n] = intensity
                heappush(q, (n, intensity))
    
    for i in summits:
        if answer[1] > visited[i]:
            answer[0] = i
            answer[1] = visited[i]
    
    return answer