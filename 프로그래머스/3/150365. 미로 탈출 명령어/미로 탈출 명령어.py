from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = ''
    
    q = deque([[x-1, y-1, '']])
    
    # 상, 하, 좌, 우
    d = {(1,0):'d', (0,-1):'l', (0,1):'r', (-1,0):'u'}
    
    result = []
    
    def distance(x, y):
        return abs(x-(r-1)) + abs(y-(c-1))
    
    if distance(x-1, y-1) > k:
        return 'impossible'
    
    while q:
        x, y, z = q.popleft()
        
        if (x, y) == (r-1, c-1):
            if (k-len(z)) % 2:
                return 'impossible'
            elif len(z) == k:
                return z
        
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            
            if 0<=nx<n and 0<=ny<m:
                if distance(nx, ny) + len(z) + 1 > k:
                    continue
                q.append((nx, ny, z + d[(dx, dy)]))
                break

    return answer