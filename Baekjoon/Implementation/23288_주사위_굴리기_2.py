'''
[주사위]
- 주사위 전개도
   2
  413
   5
   6
- 주사위의 윗면 : 1, 오른쪽 : 3
- 초기 주사위 이동방향 : 오른쪽

[주사위 이동 사이클]
(A: 주사위 아랫면의 숫자, B: 주사위 칸의 정수, C: 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수)
1. 이동 방향으로 한 칸 굴러감 (칸이 없다면, 이동 방향 반대로 한 칸 굴러감)
2. 도착한 칸에 대한 점수 획득
    2-1. 점수 = B * C
    2-2. 이동할 수 있는 칸에는 모두 정수 B 있어야 함
3. 이동방향 결정
    3-1. A > B : 이동 방향 오른쪽으로 90도 회전
    3-2. A < B : 이동 방향 왼쪽으로 90도 회전
    3-3. A = B : 방향 그대로
'''

from collections import deque

N, M, K = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]

# 동 남 서 북
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cur_d = 0

# [윗, 앞, 오른, 왼, 뒤, 아래]
dice = [1, 2, 3, 4, 5, 6]

# 주사위 이동 맵
roll_map = [
    [3, 1, 0, 5, 4, 2],  # 동
    [1, 5, 2, 3, 0, 4],  # 남
    [2, 1, 5, 0, 4, 3],  # 서
    [4, 0, 2, 3, 5, 1]   # 북
]

# 현재 위치
x, y = 0, 0

# bfs
score_map = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

# 주사위 이동
def move_dice(d):
    global dice
    dice = [dice[i] for i in roll_map[d]]

# 점수 계산
def get_score(i, j):
    q = deque([(i, j)])
    visited[i][j] = True
    val = mp[i][j]
    cells = [(i, j)]

    while q:
        ci, cj = q.popleft()
        for di, dj in dir:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M:
                if not visited[ni][nj] and mp[ni][nj] == val:
                    visited[ni][nj] = True
                    q.append((ni, nj))
                    cells.append((ni, nj))

    score = len(cells) * val
    for ci, cj in cells:
        score_map[ci][cj] = score

# 전체 맵 점수 계산
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            get_score(i, j)

# 방향 결정
def decide_dir(a, b, d):
    if a > b:
        return (d + 1) % 4
    elif a < b:
        return (d - 1) % 4
    return d

answer = 0

for _ in range(K):

    # 다음 위치 갱신
    nx = x + dir[cur_d][0]
    ny = y + dir[cur_d][1]

    if not (0 <= nx < N and 0 <= ny < M):
        cur_d = (cur_d + 2) % 4
        nx = x + dir[cur_d][0]
        ny = y + dir[cur_d][1]

    # 주사위 이동
    x, y = nx, ny
    move_dice(cur_d)

    # 점수 계산
    answer += score_map[x][y]

    # 방향 갱신
    A = dice[5]
    B = mp[x][y]
    cur_d = decide_dir(A, B, cur_d)

print(answer)