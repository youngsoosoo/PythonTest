### 문제 인식 ###
# 상, 하, 좌, 우 4방향 중 한 방향으로 이동할 수 있습니다.
# 이동할 시에 미끄러져 장애물이나 맨 끝에 부딪혀야 멈출 수 있습니다.
# R에서 G까지 갈 수 있는 최단 거리를 찾아주세요
### 문제 해결 ###
# BFS 를 통해 구해야 합니다.
# G로 갈 수 있는 최단 거리를 찾아라.

from collections import deque
def solution(board):
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0 ,0]
    
    for i in range(len(board)):
        if 'R' in board[i]:
            start = (i, board[i].index('R'))
            break
    
    visited = [[0 for i in range(len(board[0]))] for _ in range(len(board))]
    visited[start[0]][start[1]] = 1
    print(visited)
    
    q = deque([start])
    while q:
        x, y = q.popleft()
        
        if board[x][y] == 'G':
            print(visited)
            return visited[x][y] - 1
        
        for i in range(4):
            nx = x
            ny = y
            
            # 끝이나 장애물을 만날 때까지 반복
            while 0 <= nx + dx[i] < len(board) and 0 <= ny + dy[i] < len(board[0]) and board[nx+dx[i]][ny+dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]
            if not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            
    return -1