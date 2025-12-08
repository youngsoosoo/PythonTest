def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    for i in range(n):
        visited = [0] * n
        answer = max(answer, dfs(i, visited, k, dungeons, 0))
    
    return answer


def dfs(idx, visited, k, dungeons, answer):
    
    if not (k >= dungeons[idx][0] and k-dungeons[idx][1] >= 0):
        return 0
    
    
    visited[idx] = 1
    answer += 1
    k -= dungeons[idx][1]
    max_answer = answer
    
    
    for i in range(len(visited)):
        if visited[i] == 0:
            max_answer = max(max_answer, dfs(i, visited[:], k, dungeons, answer))
        
    return max_answer