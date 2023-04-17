def solution(rows, columns, queries):
    answer = []
    board = [[(i*columns)+j+1 for j in range(columns)] for i in range(rows)]
    
    for query in queries:
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        tmp = board[x1][y1] # 왼쪽 위 값 저장
        small = tmp
        
        # left
        for i in range(x1+1, x2+1):
            board[i-1][y1] = board[i][y1]
            small = min(small, board[i][y1])
        # bottom
        for i in range(y1+1, y2+1):
            board[x2][i-1] = board[x2][i]
            small = min(small, board[x2][i])
        # right
        for i in range(x2-1, x1-1, -1):
            board[i+1][y2] = board[i][y2]
            small = min(small, board[i][y2])
        # top
        for i in range(y2-1, y1-1, -1):
            board[x1][i+1] = board[x1][i]
            small = min(small, board[x1][i])
        board[x1][y1+1] = tmp
        
        answer.append(small)
        
    return answer