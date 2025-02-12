N, K = map(int, input().split())

dp  = [[] for _ in range(N+1)]
# dp[i] = i를 만드는데 가능한 경우의 수

for i in range(1, N+1):
    dp[N].append([i])

    # for j in range(i):

print(dp)