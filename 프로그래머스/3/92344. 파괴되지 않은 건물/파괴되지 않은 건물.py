def solution(board, skill):
    answer = 0
    
    visited = [[0 for i in range(len(board[0])+1)] for i in range(len(board)+1)]
    
    for _type, r1, c1, r2, c2, degree in skill:
        if _type == 2:
            visited[r1][c1] += degree
            visited[r2+1][c2+1] += degree
            visited[r1][c2+1] -= degree
            visited[r2+1][c1] -= degree
        else:
            visited[r1][c1] -= degree
            visited[r2+1][c2+1] -= degree
            visited[r1][c2+1] += degree
            visited[r2+1][c1] += degree
        
    for i in range(len(board)):
        for j in range(len(board[0])):
            visited[i][j+1] += visited[i][j]
            
    for j in range(len(board[0])):
        for i in range(len(board)):
            visited[i+1][j] +=  visited[i][j]
            
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += visited[i][j]
            
            if board[i][j] > 0:
                answer+=1
                
    return answer