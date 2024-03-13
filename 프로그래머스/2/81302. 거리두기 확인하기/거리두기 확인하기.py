from collections import deque
def solution(places):
    answer = []
    
    d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    
    def bfs(place):
        p_arr = []
        
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    p_arr.append([x, y])
                    
        for p in p_arr:
            q = deque([p])
            visited = [[0 for i in range(5)] for i in range(5)]
            distancing = [[0 for i in range(5)] for i in range(5)]
            visited[p[0]][p[1]] = 1
            
            while q:
                x, y = q.popleft()
                
                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy
                    
                    if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:
                        if place[nx][ny] == 'O':
                                q.append([nx, ny])
                                visited[nx][ny] = 1
                                distancing[nx][ny] = distancing[x][y] + 1
                        if place[nx][ny] == 'P' and distancing[x][y] <= 1:
                            return 0
                        
        return 1
    
    for place in places:
        result = bfs(place)
        answer.append(result)
    
    return answer