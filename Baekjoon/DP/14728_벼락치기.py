N, T = map(int, input().split())  # 단원 수, 총 시간
dp = [[0, 0] for _ in range(N+1)]  # 공부하기, 안하기

for i in range(1, 1+N):
    K, S = map(int, input().split())  # 공부시간, 배점

    # i를 공부하는 경우
    dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + S

    # i를 공부하지 않는 경우
    dp[i][0] = max(dp[i-1][0], dp[i-1][1])

print(dp)
print(max(dp[N][0], dp[N][1]))