from collections import deque
def solution(maps):
    answer = []
    l = len(maps)
    li = len(maps[0])
    for i in range(l):
        maps[i] = list(maps[i])
    
    
    visited = [[0 if maps[i][j] != 'X' else 1 for j in range(li)] for i in range(l)]
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    for i in range(l*li):
        q = deque([])
        cnt = 0
        if not visited[i//li][i%li]:
            q.append((i//li, i%li))
            cnt += int(maps[i//li][i%li])
            visited[i//li][i%li] = 1
        while q:
            x, y = q.popleft()
            
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                
                if 0 <= nx < l and 0 <= ny < li and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += int(maps[nx][ny])
                    maps[nx][ny] = str(cnt)
        
        if cnt != 0:
            answer.append(cnt)
        
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)