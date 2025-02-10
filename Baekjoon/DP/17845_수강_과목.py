N, K = map(int, input().split()) # 최대 공부 시간, 과목 수
dp = [0] * (N+1)

for _ in range(K):
    I, T = map(int, input().split())

    for i in range(N, T-1, -1):
        dp[i] = max(dp[i-T] + I, dp[i])

print(dp[N])