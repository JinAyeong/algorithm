'''
타일 붙일수 있는 경우
00, 1
'''

N = int(input())
dp = [0] * (N+1)
dp[0] = 1

for i in range(1, N+1):

    # 0붙일 경우
    if 0 <= i-2:
        dp[i] = (dp[i-2] + dp[i]) % 15746

    # 1붙일 경우
    dp[i] = (dp[i-1] + dp[i]) % 15746

print(dp[N] % 15746)