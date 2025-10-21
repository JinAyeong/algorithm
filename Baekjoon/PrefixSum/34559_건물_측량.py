'''
건물
1. 1로 표현된칸
2. 0으로 표현된 칸 중, 0으로 너비우선탐색했을 때 테두리에 도달할 수 없는 칸

새 건물 지을 수 있는 조건
- 두 좌표로 만들어지는 직사각형에 건물이 포함되지 않아야함
'''

from collections import deque

N, M = map(int, input().split())
mp = [list(map(int, list(input()))) for _ in range(N)]
building = [[True] * M for _ in range(N)]
building[0][0] = 0
q = deque([(0, 0)])

while q:
    ci, cj = q.popleft()

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = ci + di, cj + dj

        if 0 <= ni < N and 0 <= nj < M and mp[ni][nj] == 0 and building[ni][nj] == 1:
            q.append((ni, nj))
            building[ni][nj] = 0

prefix = [[0] * (M+1) for _ in range(N+1)]

for r in range(1, N+1):
    for c in range(1, M+1):
        cur_building = (1 if building[r-1][c-1] else 0)
        prefix[r][c] = cur_building + prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1]

for _ in range(int(input())):
    r1, c1, r2, c2 = map(int, input().split())
    building_cnt = prefix[r2][c2] - prefix[r1-1][c2] - prefix[r2][c1-1] + prefix[r1-1][c1-1]

    if building_cnt > 0:
        print(f'No {building_cnt}')
    else:
        print('Yes')