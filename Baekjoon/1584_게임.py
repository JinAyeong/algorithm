from heapq import heappush, heappop

board = [[0] * 501 for _ in range(501)]
distance = [[float('inf')] * 501 for _ in range(501)]  # 각 지점까지의 최소 생명값

# 위험 구역 1
N = int(input())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(min(x1, x2), max(x1, x2) + 1):  # x1, x2 범위 고려
        for c in range(min(y1, y2), max(y1, y2) + 1):  # y1, y2 범위 고려
            board[r][c] = 1  # 위험 구역

# 죽음 구역 2
M = int(input())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(min(x1, x2), max(x1, x2) + 1):  # x1, x2 범위 고려 !!! +1 해주기
        for c in range(min(y1, y2), max(y1, y2) + 1):
            board[r][c] = 2  # 죽음 구역

pq = [(0, 0, 0)]  # 생명값, xy
distance[0][0] = 0

# 4방향 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while pq:
    life, x, y = heappop(pq)

    if (x, y) == (500, 500):
        print(life)
        exit(0)

    # 이미 처리한 지점 continue
    if distance[x][y] < life:
        continue

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 범위를 벗어나지 않고, 죽음 구역이 아니면
        if 0 <= nx < 501 and 0 <= ny < 501 and board[nx][ny] != 2:
            next_life = life + board[nx][ny]  # 현재 위치의 생명값에 위험 구역 페널티 추가

            # 더 적은 생명값으로 해당 지점에 도달할 수 있으면 갱신
            if next_life < distance[nx][ny]:
                distance[nx][ny] = next_life
                heappush(pq, (next_life, nx, ny))

print(-1)
