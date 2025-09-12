N, M, K = map(int, input().split())

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[1][1] = 1

a = ((K - 1) // M + 1 if K else N)
b = ((K - 1) % M + 1 if K else M)

for i in range(1, a+1):
    for j in range(1, b+1):
        if (i, j) == (1, 1):
            continue
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

for k in range(a, N+1):
    for l in range(b, M+1):
        if (k, l) == (a, b):
            continue
        dp[k][l] = dp[k-1][l] + dp[k][l-1]

print(dp[N][M])