N = int(input())
mp = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):

        if not dp[i][j] or not mp[i][j]:
            continue

        d = mp[i][j]

        if 0 <= i + d < N:
            dp[i+d][j] += dp[i][j]
        if 0 <= j + d < N:
            dp[i][j+d] += dp[i][j]

print(dp[N-1][N-1])