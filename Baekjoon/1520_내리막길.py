M, N = map(int, input().split())  # 세로, 가로
land = [list(map(int, input().split())) for _ in range(M)]
route_count = [[0] * N for _ in range(M)]

# TODO