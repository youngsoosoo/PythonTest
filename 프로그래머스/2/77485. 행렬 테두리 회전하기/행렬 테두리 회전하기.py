def create_graph(n, m):
    graph = [[0 for _ in range(m)] for _ in range(n)]
    a = 1
    for i in range(n):
        for j in range(m):
            graph[i][j] = a
            a += 1
    return graph

def solution(rows, columns, queries):
    answer = []
    
    graph = create_graph(rows, columns)
    
    for x1, y1, x2, y2 in queries:
        # 시작점(x1-1, y1-1)
        temp = graph[x1-1][y1-1]
        result = temp
        
        for i in range(x1-1, x2-1):
            tmp = graph[i+1][y1-1]
            graph[i][y1-1] = tmp
            result = min(result, tmp)
            
        for i in range(y1-1, y2-1):
            tmp = graph[x2-1][i+1]
            graph[x2-1][i] = tmp
            result = min(result, tmp)
            
        for i in range(x2-1, x1-1, -1):
            tmp = graph[i-1][y2-1]
            graph[i][y2-1] = tmp
            result = min(result, tmp)
            
        for i in range(y2-1, y1-1, -1):
            tmp = graph[x1-1][i-1]
            graph[x1-1][i] = tmp
            result = min(result, tmp)
        
        graph[x1-1][y1] = temp
        answer.append(result)
    
    return answer