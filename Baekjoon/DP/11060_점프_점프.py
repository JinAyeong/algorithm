N = int(input())
arr = list(map(int, input().split()))
dp = [float('inf')] * N
dp[0] = 0

for i in range(N):
    jump = arr[i]

    for j in range(1, jump+1):
        if i + j <= N-1:
            dp[i + j] = min(dp[i + j], dp[i] + 1)

print(dp[N-1] if dp[N-1] != float('inf') else -1)