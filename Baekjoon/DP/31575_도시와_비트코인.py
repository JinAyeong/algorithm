N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(M)]
dp = [[False] * (N+1) for _ in range(M+1)]
dp[1][1] = True

for i in range(1, M+1):
    for j in range(1, N+1):
        if mp[i-1][j-1] == 0:
            continue
        if dp[i - 1][j] or dp[i][j - 1]:
            dp[i][j] = True

print('Yes' if dp[M][N] != 0 else 'No')