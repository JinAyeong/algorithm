'''
go k: 현재 방향으로 1, 2, 3 칸만큼 이동
turn dir: 왼쪽, 오른쪽으로 회전
'''

from collections import deque

M, N = map(int, input().split())  # 세로, 가로
mp = [list(map(int, input().split())) for _ in range(M)]
sr, sc, sd = map(int, input().split())
er, ec, ed = map(int, input().split())
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 오른쪽, 왼쪽, 아래, 위
next_direction = [(2, 3), (2, 3), (0, 1), (0, 1)]

visited = [[[False] * 4 for _ in range(N)] for _ in range(M)]
visited[sr-1][sc-1][sd-1] = True
q = deque([(sr-1, sc-1, sd-1, 0)])

while q:
    cr, cc, cd, cnt = q.popleft()

    if (cr, cc, cd) == (er-1, ec-1, ed-1):
        print(cnt)
        break

    # 전진
    for k in range(1, 4):
        nr, nc = cr + direction[cd][0] * k, cc + direction[cd][1] * k

        if not (0 <= nr < M and 0 <= nc < N) or mp[nr][nc]:
            break
        if visited[nr][nc][cd]:
            continue
        visited[nr][nc][cd] = True
        q.append((nr, nc, cd, cnt + 1))

    # 회전
    for nd in next_direction[cd]:
        if not visited[cr][cc][nd]:
            visited[cr][cc][nd] = True
            q.append((cr, cc, nd, cnt + 1))