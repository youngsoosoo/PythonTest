import heapq, sys
def solution(n, s, a, b, fares):
    answer = sys.maxsize
    graph = [[] for i in range(n+1)]
    
    for a1, b1, c in fares:
        graph[a1].append([b1, c])
        graph[b1].append([a1, c])
    
    def dij(start):
        distance = [sys.maxsize for i in range(n+1)]
        distance[start] = 0
        hq = [[0, start]]
        
        while hq:
            dis, node = heapq.heappop(hq)
            
            if distance[node] < dis:
                continue
            
            for dnode, ddis in graph[node]:
                if distance[dnode] > dis + ddis:
                    distance[dnode] = dis + ddis
                    heapq.heappush(hq, (dis + ddis, dnode))
        return distance
        
    d = [0] + [dij(i) for i in range(1, n+1)]
    
    for i in range(1, n+1):
        answer = min(answer, (d[i][s] + d[i][a] + d[i][b]))
    
    return answer