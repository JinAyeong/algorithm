N = int(input())

dp = [[0] * 10 for _ in range(N)] # [i][j] : 왼쪽에서 i+1번째 자리 수에 오는 j의 수

dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, N):

    for j in range(10):
        up = (dp[i-1][j+1] if j+1 < 10 else 0)
        down = (dp[i-1][j-1] if 0 <= j-1 else 0)

        dp[i][j] = (up + down) % 1000000000

print(sum(dp[N-1]) % 1000000000)