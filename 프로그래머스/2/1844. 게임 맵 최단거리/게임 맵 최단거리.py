from collections import deque
def solution(maps):
    answer = -1
    len_maps = len(maps)
    len_m = len(maps[0])
    
    visited = [[0 for i in range(len_m)] for i in range(len_maps)]
    
    d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    
    visited[0][0] = 1
    q = deque([[0, 0]])
    while q:
        x, y = q.popleft()
        
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < len_maps and 0 <= ny < len_m and maps[nx][ny]:
                if not visited[nx][ny] or visited[x][y] + 1 < visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
    
    if visited[len_maps-1][len_m-1]:
        answer = visited[len_maps-1][len_m-1]
    return answer