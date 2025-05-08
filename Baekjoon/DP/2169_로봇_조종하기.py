'''
1. 왼쪽, 오른쪽, 아래로 이동가능
2. 왼쪽에서 오는 경우, 오른쪽에서 오는 경우 다 처리해줘야 하기 떄문에 한 줄씩 탐색 후 합쳐준다
'''

N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]

dp = [[-float('inf')] * M for _ in range(N)]
dp[0][0] = mp[0][0]

# 맨 윗줄 : 오른쪽으로만 이동 가능
for i in range(1, M):
    dp[0][i] = max(dp[0][i-1], dp[0][i]) + mp[0][i]

for i in range(1, N):

    row_r = [-float('inf')] * M
    row_l = [-float('inf')] * M

    # 오른쪽으로 이동
    row_r[0] = dp[i-1][0] + mp[i][0]
    for j in range(1, M):
        row_r[j] = max(row_r[j], row_r[j-1], dp[i-1][j]) + mp[i][j]

    # 왼쪽으로 이동
    row_l[M-1] = dp[i-1][M-1] + mp[i][M-1]
    for j in range(M-2, -1, -1):
        row_l[j] = max(row_l[j], row_l[j+1], dp[i-1][j]) + mp[i][j]

    # 둘 중 더 큰 값
    for j in range(M):
        dp[i][j] = max(row_r[j], row_l[j])

print(dp[N-1][M-1])