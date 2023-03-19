def solution(dirs):
    d = {"U" : [1, 0], "D" : [-1, 0], "R" : [0, 1], "L" : [0, -1]}
    visited = [[0for i in range(10)] for i in range(10)]
    x, y = 0, 0
    visited = set()
    for i in  dirs:
        dx, dy = d[i]
        nx = x + dx
        ny = y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((nx, ny, x, y))
            visited.add((x, y, nx, ny))
            x, y = nx, ny
        
        

    return len(visited)//2