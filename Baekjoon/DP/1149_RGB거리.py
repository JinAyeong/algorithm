N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
dp = cost[0]

for i in range(1, N):

    # i 번째 집 빵간색
    red = min(dp[1] + cost[i][0], dp[2] + cost[i][0])

    # i 번째 집 초록색
    green = min(dp[0] + cost[i][1], dp[2] + cost[i][1])

    # i 번째 집 파란색
    blue = min(dp[0] + cost[i][2], dp[1] + cost[i][2])

    dp[0], dp[1], dp[2] = red, green, blue

print(min(dp))