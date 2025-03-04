N = int(input())
dp = [float('inf')] * (N+1)
coins = [1, 2, 5, 7]

dp[0] = 0

for i in range(1, N+1):
    for coin in coins:
        if 0 <= i-coin < N:
            dp[i] = min(dp[i-coin]+1, dp[i])

print(dp[N])