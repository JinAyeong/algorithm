def solution(m, n, puddles):
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for px, py in puddles:
        dp[py][px] = -1
    
    for x in range(1, n+1):
        for y in range(1, m+1):
            
            if dp[x][y] == -1 or (x, y) == (1, 1):
                continue
            
            dp[x][y] = (max(0, dp[x-1][y]) + max(0, dp[x][y-1])) % 1000000007

    
    return dp[n][m]