from heapq import heappop, heappush

# 초코바 : #, 주난이 : *
# 빈공강 : "0", 친구 : "1"

N, M = map(int, input().split())  # 세로, 가로
x1, y1, x2, y2 = map(int, input().split())  # 주난 xy, 범인 xy
classroom = [list(input()) for _ in range(N)]

# 방문표시
visited = [[float('inf')] * M for _ in range(N)]
visited[x1-1][y1-1] = 0

# 방문했으면 continue
# 방문하지 않았을때 1이면 방문처리, 점프 계산 -> heap 에 append
# 방문하지 않았을때 0이면 방문처리 -> heap에 append
# pop했을때 x2, y2이면 break

pq = []
heappush(pq, (0, x1-1, y1-1))  # 점프수, x, y

while pq:

    cur_jump, cur_x, cur_y = heappop(pq)  # 현재 파동

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

        nx, ny = cur_x + di, cur_y + dj

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        # 방문했으면 continue
        if visited[nx][ny] != float('inf'):
            continue

        if classroom[nx][ny] == '#':
            print(cur_jump + 1)
            exit(0)

        # 빈공간이고, 더 짧은 거리가 있으면 heappush
        if classroom[nx][ny] == '0' and visited[nx][ny] > cur_jump:
            heappush(pq, (cur_jump, nx, ny))
            visited[nx][ny] = cur_jump

        # 친구가 있으면 쓰러트리고 heappush
        if classroom[nx][ny] == '1' and visited[nx][ny] > cur_jump + 1:
            heappush(pq, (cur_jump+1, nx, ny))
            visited[nx][ny] = cur_jump + 1