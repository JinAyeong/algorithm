from collections import deque

def bfs(i, j, N, M, mp, visited):

    q = deque([(i, j)])

    while q:
        ci, cj = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and mp[ni][nj] == '#':
                visited[ni][nj] = True
                q.append((ni, nj))


def solve():

    N, M = map(int, input().split())
    mp = [list(input()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    result = 0

    for x in range(N):
        for y in range(M):
            if mp[x][y] == "#" and not visited[x][y]:
                visited[x][y] = True
                bfs(x, y, N, M, mp, visited)
                result += 1

    print(result)


for _ in range(int(input())):
    solve()