from collections import deque

# . : 비어있는곳, * : 물, X : 돌, D : 도착, S : 시작


R, C = map(int, input().split())  # R행, C열
forest = [list(input()) for _ in range(R)]

start = deque([])
end = (0, 0)
water = deque([])

water_time = [[float('inf')] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]

for i in range(R):
    for j in range(C):

        if forest[i][j] == '*':
            water.append((i, j, 0))
            water_time[i][j] = 0
        elif forest[i][j] == 'S':
            start.append((i, j, 0))
            visited[i][j] = True
        elif forest[i][j] == 'D':
            end = (i, j)


# 물 차오르는 곳 먼저 전부 water_time 2차원 배열에 따로 저장
while water:

    cr, cc, ct = water.popleft()

    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nr, nc = cr + di, cc + dj

        if 0 <= nr < R and 0 <= nc < C and forest[nr][nc] == '.' and water_time[nr][nc] == float('inf'):
            water_time[nr][nc] = ct + 1
            water.append((nr, nc, ct + 1))


# 고슴도치 이동
while start:

    cr, cc, ct = start.popleft()

    # 도착이면 마무리
    if (cr, cc) == end:
        print(ct)
        exit(0)

    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nr, nc = cr + di, cc + dj

        # 고슴도치가 이동 가능할 때
        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and (forest[nr][nc] == '.' or forest[nr][nc] == 'D'):

            # 도착이거나, 아직 물에 차치않은 곳이면 방문처리, append
            if forest[nr][nc] == 'D' or water_time[nr][nc] > ct + 1:
                visited[nr][nc] = True
                start.append((nr, nc, ct + 1))


print('KAKTUS')



# -----------------실패 코드--------------------------------------
# . : 비어있는곳, * : 물, X : 돌, D : 도착, S : 시작


R, C = map(int, input().split())  # R행, C열
forest = [list(input()) for _ in range(R)]

start = deque([])
end = (0, 0)
water = deque([])

# 지도 위치 기록
for i in range(R):
    for j in range(C):

        if forest[i][j] == '*':
            water.append((i, j, 0))
        elif forest[i][j] == 'S':
            start.append((i, j, 0))
        elif forest[i][j] == 'D':
            end = (i, j)


# 물 차오르는 곳 먼저 전부 지도에 갱신
while water:

    cr, cc, ct = water.popleft()

    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nr, nc = cr + di, cc + dj

        if 0 <= nr < R and 0 <= nc < C and forest[nr][nc] == '.':
            forest[nr][nc] = ct + 1
            water.append((nr, nc, ct + 1))


visited = [[False] * C for _ in range(R)]
visited[start[0][0]][start[0][1]] = 0

# 고슴도치 이동
while start:

    cr, cc, ct = start.popleft()

    if (cr, cc) == end:
        print(ct)
        exit(0)


    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nr, nc = cr + di, cc + dj

        # 고슴도치가 이동 가능할 때 -> 여기서 실수 발생! : "." 일때(물이 차오르지 않는 부분)도 이동 가능
        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and isinstance(forest[nr][nc], int) and forest[nr][nc] > ct + 1:
            visited[nr][nc] = ct + 1
            start.append((nr, nc, ct + 1))

        # 고슴도치가 도착함
        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and forest[nr][nc] == 'D':
            visited[nr][nc] = ct + 1
            start.append((nr, nc, ct + 1))

print('KAKTUS')


