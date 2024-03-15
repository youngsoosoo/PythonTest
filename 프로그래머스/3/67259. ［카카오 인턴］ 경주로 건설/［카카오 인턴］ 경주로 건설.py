from collections import deque
import sys
def solution(board):
    answer = 0
    
    def bfs(start):
        q = deque([start])
        visited = [[sys.maxsize for i in range(len(board))] for i in range(len(board))]
        visited[0][0] = 0
        d = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while q:
            x, y, beforCost, z = q.popleft()
            for i in range(4):
                nx = x + d[i][0]
                ny = y + d[i][1]

                if 0 <= nx < len(board) and 0 <= ny < len(board) and not board[nx][ny]:
                    if z == i:
                        cost = beforCost + 100
                    else:
                        cost = beforCost + 600

                    if visited[nx][ny] > cost:
                        q.append([nx, ny, cost, i])
                        visited[nx][ny] = cost
    
        return visited[-1][-1]
    return min(bfs([0, 0, 0, 0]), bfs([0, 0, 0, 3]))