### 문제 인식 ###
# 파일을 정리하려고 합니다.
# 왼쪽 상단부터 오른쪽 하단까지 드래그하고,
# 이때, 모든 파일이 드래그 안에 담겨야 합니다.
# 드래그의 첫점과 끝점을 return
### 문제 해결 방법 ###
# O(n^2) 이상으로 풀어도 됌.

def solution(wallpaper):
    answer = [51, 51, 0, 0]
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                answer[0] = min(answer[0], i)
                answer[1] = min(answer[1], j)
                answer[2] = max(answer[2], i+1)
                answer[3] = max(answer[3], j+1)
                
    return answer