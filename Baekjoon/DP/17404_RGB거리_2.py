N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

answer = float('inf')

for first in range(3):
    dp = [[float('inf')] * 3 for _ in range(N)]
    
    # 첫 번째 집 색 선택
    dp[0][first] = costs[0][first]
    
    # 2 ~ N-1번째 집 색 선택
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    # 마지막 집 색 선택
    for last in range(3):
        if last != first:
            answer = min(answer, dp[N-1][last])

print(answer)
