import sys
sys.setrecursionlimit(10**6)

M, N = map(int, input().split())  # 세로, 가로
land = [list(map(int, input().split())) for _ in range(M)]
route_count = [[-1] * N for _ in range(M)]

# 상하좌우 내리막길이 있을때만 이동
# 다음 경로 += 현재 경로

# r, c 에서 시작해서 M-1, N-1에 도착
def move(r, c):

    if (r, c) == (M-1, N-1):
        # print('도착')
        # for line in route_count:
        #     print(*line)
        return 1

    if route_count[r][c] != -1:
        return route_count[r][c]

    route_count[r][c] = 0
    # print('초기화')
    # for line in route_count:
    #     print(*line)

    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nr, nc = r + di, c + dj

        if 0 <= nr < M and 0 <= nc < N and land[nr][nc] < land[r][c]:
            route_count[r][c] += move(nr, nc)

    # print((r, c))
    # for line in route_count:
    #     print(*line)

    return route_count[r][c]

print(move(0, 0))