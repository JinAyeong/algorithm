N = int(input())

dp = [[0] * 10 for _ in range(N+1)] # dp[i][j] : i자리수에서 첫 숫자가 j인 오르막 개수

dp[1] = [1] * 10

for i in range(2, N+1):
    # for j in range(10):
    #     dp[i][j] = (sum(dp[i-1][j:])) % 10007

    # 누적합으로 변경
    dp[i][9] = dp[i-1][9]
    for j in range(8, -1, -1):
        dp[i][j] = (dp[i-1][j] + dp[i][j+1]) % 10007

print(sum(dp[N]) % 10007)