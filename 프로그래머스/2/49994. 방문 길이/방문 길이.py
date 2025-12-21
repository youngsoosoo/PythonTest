from collections import deque
def solution(dirs):
    sets = set()
    d = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
    x, y = 0, 0
    
    for di in dirs:
        dx, dy = d[di]
        nx = x + dx
        ny = y + dy
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            sets.add(((x, y), (nx, ny)))
            sets.add(((nx, ny), (x, y)))
            x = nx
            y = ny
            
        
    return len(sets) // 2