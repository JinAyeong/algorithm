# topdown dp

# 런타임에러 오류 리커전 에러인거 까먹었다...
import sys
sys.setrecursionlimit(10**6)

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(N)] # dp[x][y] = (x, y)에서 갈 수 있는 최대 칸 수
result = 0

def eat(i, j):
    global result

    # 이미 답 있으면 그거 return
    if dp[i][j] != -1:
        return dp[i][j]

    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = [0] * 4

    # 상하좌우 돌면서 어떤 곳으로 가야 max인지 체크
    for idx in range(4):
        ni, nj = i + d[idx][0], j + d[idx][1]

        if 0 <= ni < N and 0 <= nj < N and forest[ni][nj] > forest[i][j]: # 조건에 맞을 떼
            if dp[ni][nj] != -1: # 옆칸 이미 계산했던 곳이면 그 칸 + 1
                cnt[idx] += dp[ni][nj] + 1
            else: # 옆칸 안가본 곳이면 dfs
                cnt[idx] += eat(ni, nj) + 1

    dp[i][j] = max(cnt)

    return dp[i][j]

for a in range(N):
    for b in range(N):
        result = max(eat(a, b), result)

print(result + 1)