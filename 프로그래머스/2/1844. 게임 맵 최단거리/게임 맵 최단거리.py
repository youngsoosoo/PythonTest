from collections import deque
def solution(maps):
    
    if not maps[0][0]:
        return -1
    
    n, m = len(maps), len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    # 상, 하, 좌, 우
    d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    
    q = deque()
    q.append((0, 0, 1))
    
    while q:
        x, y, z = q.popleft()
        
        
        # 맵의 끝에 도달했을 때
        if x == n-1 and y == m-1:
            return z
        
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, z + 1))
                    
    
    return -1