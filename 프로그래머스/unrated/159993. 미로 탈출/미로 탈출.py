### 문제 인식 ###
# 직사각형 미로 탈출
# S는 시작점,L은 레버(레버를 들러야 탈출할 수 있다.)
### 문제 해결 ###
# 먼저 레버가 있는 곳으로 BFS를 통해 가고,
# 레버 이후에 다시 방향을 EXIT로 잡고 BFS를 통해
# 최소 거리를 구합니다.
from collections import deque

def bfs(start, end, maps):
	# 탐색할 방향
    dy = [0, 1, -1, 0]
    dx = [1, 0, 0, -1]
    
    n = len(maps)       # 세로
    m = len(maps[0])    # 가로
    visited = [[False for i in range(m)] for _ in range(n)]
    q = deque()
    
    # 초깃값 설정
    for i in range(n):
        for j in range(m):
            if maps[i][j] == start:      
                q.append((i, j, 0))
                visited[i][j] = True
                break 
        if q: break
    
    while q:
        x, y, cost = q.popleft()
        
        if maps[x][y] == end:
            return cost
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # maps 범위내에서 벽이 아니라면 지나갈 수 있음
            if 0<= nx <n and 0<= ny <m and maps[nx][ny] !='X':
                if not visited[nx][ny]:	# 아직 방문하지 않는 통로라면
                    q.append((nx, ny, cost+1))
                    visited[nx][ny] = True
                    
    return -1	# 탈출할 수 없다면

def solution(maps):
    
    cnt1 = bfs('S', 'L', maps)
    cnt2 = bfs('L', 'E', maps)
    
    if cnt1 != -1 and cnt2 != -1:
        return cnt1+cnt2

    return -1