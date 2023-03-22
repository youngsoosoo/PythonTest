from collections import deque
def solution(m, n, board):
    answer = 0
    
    for i in range(m):
        board[i] = list(board[i])
        
    while True:
        block = set()
        #R, M, A, F, N, T, J ,C
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '':
                    continue
                
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    block.add((i, j))
                    block.add((i+1, j))
                    block.add((i, j+1))
                    block.add((i+1, j+1))

        if len(block) == 0 :
            break
        block = list(block)
        block.sort()
        for x, y in block:
            answer+=1
            while x-1 >= 0 :
                board[x][y] = board[x-1][y]
                board[x-1][y] = ''
                x-=1

                    
            
    return answer