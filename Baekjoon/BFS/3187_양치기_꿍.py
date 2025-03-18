'''
양들의 수 > 늑대의 수 : 늑대가 잡아먹힘
그 외 : 양이 잡아먹힘
'''
from collections import deque

R, C = map(int, input().split())
mp = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

def bfs(x, y):

    q = deque([(x, y)])
    visited[x][y] = True
    sheep = 0
    wolf = 0
    if mp[x][y] == 'v':
        wolf += 1
    elif mp[x][y] == 'k':
        sheep += 1

    while q:
        cx, cy = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and mp[nx][ny] != '#':
                visited[nx][ny] = True
                q.append((nx, ny))
                if mp[nx][ny] == 'v':
                    wolf += 1
                elif mp[nx][ny] == 'k':
                    sheep += 1

    return sheep, wolf

sheep, wolf = 0, 0

for i in range(R):
    for j in range(C):
        if not visited[i][j] and mp[i][j] != '#':
            s, w = bfs(i, j)
            if s > w:
                sheep += s
            else:
                wolf += w

print(sheep, wolf)