def solution(board):
    answer = 0
    
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 1:
                board[i][j] = 1 + min(board[i-1][j-1], board[i-1][j], board[i][j-1])
    
    for i in board:
        answer = max(max(i), answer)
        
    return answer**2