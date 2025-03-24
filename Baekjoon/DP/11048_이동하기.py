N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = mp[0][0]

for i in range(N):
    for j in range(M):
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + mp[i][j])
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + mp[i][j])
        if i > 0 and j > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + mp[i][j])

print(dp[N-1][M-1])