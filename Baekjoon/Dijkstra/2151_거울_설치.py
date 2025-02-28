from heapq import heappop, heappush

N = int(input())
mp = [list(input()) for _ in range(N)]

# 거울을 만나면 왼쪽으로 90도 또는 오른쪽으로 90도 틀어서 방향 꺾기
# heap에 거울 수 추가해서 push

heap = []
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = [[[float('inf') for _ in range(4)] for _ in range(N)] for _ in range(N)]
result = float('inf')

# 문 찾기
for x in range(N):
    if heap:
        break
    for y in range(N):
        if mp[x][y] == '#':
            visited[x][y][0] = visited[x][y][1] = visited[x][y][2] = visited[x][y][3] = 0
            heappush(heap, (0, 0, x, y))
            heappush(heap, (0, 1, x, y))
            heappush(heap, (0, 2, x, y))
            heappush(heap, (0, 3, x, y))
            break

# 거울 설치
while heap:
    cnt, cd, cx, cy = heappop(heap)

    nx, ny = cx + direction[cd][0], cy + direction[cd][1]

    if not (0 <= nx < N and 0 <= ny < N):
        continue

    # 지나가기
    if mp[nx][ny]== '.' and cnt <= visited[nx][ny][cd]:
        heappush(heap, (cnt, cd, nx, ny))
        visited[nx][ny][cd] = cnt

    # 거울 설치 가능 구영
    elif mp[nx][ny] == '!':
        # 1. 그냥 지나가기
        heappush(heap, (cnt, cd, nx, ny))
        visited[nx][ny][cd] = cnt
        # 2. 오른쪽으로 회전
        if cnt+1 <= visited[nx][ny][(cd + 1) % 4]:
            heappush(heap, (cnt + 1, (cd + 1) % 4, nx, ny))
            visited[nx][ny][(cd + 1) % 4] = cnt + 1
        # 3. 왼쪽으로 회전
        if cnt+1 <= visited[nx][ny][(cd - 1) % 4]:
            heappush(heap, (cnt + 1, (cd - 1) % 4, nx, ny))
            visited[nx][ny][(cd - 1) % 4] = cnt + 1

    # 문 도착
    elif mp[nx][ny] == '#' and visited[nx][ny][cd] == float('inf'):
        print(cnt)
        break