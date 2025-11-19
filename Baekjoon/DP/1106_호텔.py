C, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [float('inf')] * 1102 # dp[c] = c명을 늘이기 위해 필요한 돈의 최솟값
dp[0] = 0
result = float('inf')

for cost, gain in arr:

    for i in range(1, 1102):

        dp[i] = min(dp[i-gain] + cost, dp[i])
        if i >= C:
            result = min(result, dp[i])

print(result)