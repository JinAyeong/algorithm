n, m = map(int, input().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[1][1] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        for di, dj in [(-1, 0), (0, -1), (-1, -1)]:
            dp[i][j] += (dp[i + di][j + dj]) % (10**9 + 7)

print(dp[n][m] % (10**9 + 7))