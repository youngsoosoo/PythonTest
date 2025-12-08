answer = 0
n = 0
visited = []

def solution(k, dungeons):
    global n, visited
    
    n = len(dungeons)
    visited = [0] * n
    
    dfs(k, 0, dungeons)
    
    return answer


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt
    
    for j in range(n):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0