def solution(triangle):
    answer = 0
    dp = triangle

    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            #처음일 때
            if j == 0:
                dp[i][j] = triangle[i][j] + triangle[i-1][j]
            #끝일 때
            elif j == len(triangle[i])-1:
                dp[i][j] = triangle[i][j] + triangle[i-1][j-1]
            else:
                dp[i][j] = triangle[i][j] + max(triangle[i-1][j], triangle[i-1][j-1])
    answer = max(dp[-1])
        
    return answer