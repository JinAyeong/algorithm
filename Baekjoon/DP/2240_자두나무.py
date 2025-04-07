T, W = map(int, input().split())
plums = [int(input()) for _ in range(T)]

# dp[i][j]: i초까지 j번 이동했을 때 최대 자두 수
dp = [[0] * (W + 1) for _ in range(T + 1)]

for i in range(1, T + 1):
    for j in range(W + 1):
        # 현재 자두가 떨어지는 나무
        plum = plums[i - 1]

        if j == 0:
            if plum == 1:
                dp[i][j] = dp[i - 1][j] + 1
            else:
                dp[i][j] = dp[i - 1][j]
        else:
            if plum == (j % 2) + 1:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])

print(max(dp[T]))
