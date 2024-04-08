def solution(n, money):
    dp = [1] + [0 for i in range(n)]
    
    for m in money:
        for i in range(m, n+1):
            dp[i] += dp[i-m]
    
    return dp[-1] % 1000000007