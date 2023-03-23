from collections import deque
def solution(maps):
    answer = -1
    q = deque([(0, 0)])
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    n, m = len(maps), len(maps[0])
    visited = [[0 for j in range(m)] for i in range(n)]
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            answer = visited[len(visited)-1][len(visited[0])-1]+1
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny]:
                if not visited[nx][ny] or visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    return answer