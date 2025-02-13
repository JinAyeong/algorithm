N, K = map(int, input().split())

# 알아야할 것 : 정수 n을 만들 때, 이전에 몇개의 수를 더했는지 알아야함
dp = [[0] * (K+1) for _ in range(N+1)] # dp[n][k] = n을 만들때 k개의 수를 더해서 만들 수 있는 경우의 수

