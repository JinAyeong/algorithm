from collections import deque

def bfs(i, j, N, M, visited, mp):
    q = deque([(i, j)])
    visited[i][j] = True
    size = 1

    while q:
        ci, cj = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and mp[ni][nj]:
                visited[ni][nj] = True
                size += 1
                q.append((ni, nj))

    return size

N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
cnt = 0
result = 0

for i in range(N):
    for j in range(M):
        if mp[i][j] and not visited[i][j]:
            cnt += 1
            result = max(result, bfs(i, j, N, M, visited, mp))

print(cnt)
print(result)