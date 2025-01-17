# n종류의 동전, 가치의 합 k, 최소 동전의 수

n, k = map(int, input().split())
dp = [float('inf')] * (k+1)
coins = [int(input()) for _ in range(n)]

dp[0] = 0

for i in range(1, k+1):

    for coin in coins:

        if 0 <= i - coin < k:
            dp[i] = min(dp[i-coin] + 1, dp[i])


if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15
# 0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 1, 2, 3, 3