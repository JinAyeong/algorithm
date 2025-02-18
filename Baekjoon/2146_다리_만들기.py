# 다리 테두리를 한겹씩 확장하면서 겹칠 떄

from collections import deque

N = int(input())
mp = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
island = deque([])

# 섬 찾기
def bfs(x, y, num):

    visited[x][y] = True
    mp[x][y] = num
    island.append((x, y, num, 0))
    q = deque([(x, y)])

    while q:
        cx, cy = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if mp[nx][ny] == 1:
                    visited[nx][ny] = True
                    mp[nx][ny] = num
                    q.append((nx, ny))
                elif mp[nx][ny] == 0:
                    island.append((nx, ny, num, 1))

cnt = 2 # 섬은 2번부터 시작

for i in range(N):
    for j in range(N):
        if mp[i][j] == 1:
            bfs(i, j, cnt)
            cnt += 1

result = float('inf')

# 다리 연결
while island:
    cx, cy, cur, d = island.popleft()
    if d >= result:
        continue

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = cx + dx, cy + dy

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] != cur:
            if mp[nx][ny] == 0:
                visited[nx][ny] = cur
                island.append((nx, ny, cur, d+1))
            elif mp[nx][ny] != cur:
                result = min(result, d)

print(result)
