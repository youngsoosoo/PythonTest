def solution(m, n, puddles):
    
    visited = [[0 for j in range(n+1)] for i in range(m+1)]
    print(visited)
    visited[1][1] = 1
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if i==1 and j==1:
                continue
            if [i, j] not in puddles:
                visited[i][j] = (visited[i-1][j] + visited[i][j-1])% 1000000007
            else :
                visited[i][j] = 0
    
    print(visited)
    return visited[m][n]