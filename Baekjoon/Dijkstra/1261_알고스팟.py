from heapq import heappop, heappush

M, N = map(int, input().split())  # 가로, 세로
mp = [list(map(int, input())) for _ in range(N)]
visited = [[float('inf')] * M for _ in range(N)]
visited[0][0] = 0
heap = [(0, 0, 0)]

while heap:

    b, x, y = heappop(heap)

    if (x, y) == (N-1, M-1):
        print(b)
        break

    if visited[x][y] < b:
        continue

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M:
            if mp[nx][ny] + b < visited[nx][ny]:
                visited[nx][ny] = mp[nx][ny] + b
                heappush(heap, (mp[nx][ny] + b, nx, ny))
