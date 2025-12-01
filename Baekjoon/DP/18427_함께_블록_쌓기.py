N, M, H = map(int, input().split()) # N명의 학생들, 최대 M개의 블록, 높이가 H인 탑 완성
students_blocks = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (H+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    blocks = students_blocks[i-1]

    for h in range(H+1):
        
        # 블록 사용 x
        dp[i][h] = dp[i-1][h]

        # 블록 사용
        for b in blocks:
            if h - b >= 0:
                dp[i][h] += dp[i-1][h-b]

        dp[i][h] %= 10007

print(dp[N][H])