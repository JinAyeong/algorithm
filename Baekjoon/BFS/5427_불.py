from collections import deque

# . 빈공간, # 벽, @ 상근이, * 불
# 빈공간만 불이 번짐
# 범위를 벗어났을 때 탈출 성공

for tc in range(int(input())):

    w, h = map(int, input().split()) # 너비, 높이
    building = [list(input()) for _ in range(h)]
    fire = []
    start = None
    visited = [[False] * w for _ in range(h)]

    # 위치 파악
    for a in range(h):
        for b in range(w):
            if building[a][b] == '*':
                fire.append((a, b, 0, '*'))
                visited[a][b] = True
            elif building[a][b] == '@':
                start = (a, b, 0, '@')
                visited[a][b] = True

    q = deque(fire + [start])

    result = False

    while q:

        cr, cc, ct, type = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = cr + di, cc + dj

            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and building[nr][nc] == '.' and type=='*':
                q.append((nr, nc, ct + 1, type))
                visited[nr][nc] = True
                building[nr][nc] = '*'

            elif 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and building[nr][nc] == '.':
                q.append((nr, nc, ct + 1, type))
                visited[nr][nc] = True

            elif type == '@' and not(0 <= nr < h and 0 <= nc < w):
                print(ct + 1)
                result = True
                break

        if result:
            break

    if not result:
        print('IMPOSSIBLE')