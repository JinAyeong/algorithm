N = int(input())
price = list(map(int, input().split()))
dp = [0] * (N+1)

for i in range(1, N+1):
    dp[i] = price[i-1]

    for j in range(1, N+1):
        dp[i] = max(dp[i-j] + dp[j], dp[i])

print(dp[N])