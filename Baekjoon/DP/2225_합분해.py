N, K = map(int, input().split())

# 알아야할 것 : 정수 n을 만들 때, 이전에 몇개의 수를 더했는지 알아야함
dp = [[0] * (N+1) for _ in range(K+1)] # dp[k][n] = n을 만들때 k개의 수를 더해서 만들 수 있는 경우의 수

# 0을 한가지 숫자로 만들 수 있는 숫자는 전부 1개
for j in range(N+1):
    dp[1][j] = 1

for i in range(2, K+1):
    for j in range(N+1):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
        dp[i][j] %= 1000000000

print(dp[K][N])