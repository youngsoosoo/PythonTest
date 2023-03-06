def solution(n):
    if n<3:
        return n
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    answer=dp[n]
    return answer%1234567