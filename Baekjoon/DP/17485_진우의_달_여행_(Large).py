N, M = map(int, input().split())
fuel = [list(map(int, input().split())) for _ in range(N)]
dp = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N)]  # [n][m][방향] (왼, 가, 오)

for d in range(M):
    dp[0][d] = [fuel[0][d]] * 3

for i in range(1, N):
    for j in range(M):

        # 완쪽으로 이동
        if 0 <= j-1 < M:
            dp[i][j][0] = min(fuel[i][j] + dp[i-1][j-1][1], fuel[i][j] + dp[i-1][j-1][2])

        # 가운데로 이동
        dp[i][j][1] = min(fuel[i][j] + dp[i-1][j][0], fuel[i][j] + dp[i - 1][j][2])

        # 오른쪽으로 이동
        if 0 <= j+1 < M:
            dp[i][j][2] = min(fuel[i][j] + dp[i-1][j+1][0], fuel[i][j] + dp[i - 1][j+1][1])

min_fuel = float('inf')

# 계산
for f in range(M):
    min_fuel = min(min_fuel, min(dp[N-1][f]))

print(min_fuel)