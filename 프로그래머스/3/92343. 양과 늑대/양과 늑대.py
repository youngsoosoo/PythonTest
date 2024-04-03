def solution(info, edges):
    answer = []
    visited = [0 for i in range(len(info))]
    
    def dfs(sheep, wolf):
        
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        
        for a, b in edges:
            if visited[a] and not visited[b]:
                visited[b] = 1
                if not info[b]:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[b] = 0
    
    visited[0] = 1
    dfs(1, 0)
    
    return max(answer)