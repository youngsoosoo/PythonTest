def solution(arr):
    # 0과 1의 개수
    answer = [0, 0]
    # 세어야 할 길이
    l = len(arr)
    
    # 반복적으로 호출할 재귀함수 구현
    def dfs(a, b, l):
        for i in range(a, a+l):
            for j in range(b, b+l):
                if arr[i][j] != arr[a][b]:
                    l = l // 2
                    dfs(a, b, l)
                    dfs(a, b+l, l)
                    dfs(a+l, b, l)
                    dfs(a+l, b+l, l)
                    return
        answer[arr[a][b]] += 1
                
    dfs(0, 0, l)
    
        
    return answer