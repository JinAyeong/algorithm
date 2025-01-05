# 1 : 1가지 (1)
# 2 : 2가지 (2, 1+1)
# 3 : 3가지 (3, 2+1, 1+1+1)
# 4 : 4가지 (3+1, 2+1+1, 1+1+1+1, 2+2)

dp = [0] * (10001)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 10001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])

for _ in range(int(input())):
    n = int(input())
    print[dp[n]]