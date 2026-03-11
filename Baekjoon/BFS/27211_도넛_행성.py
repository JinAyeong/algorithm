'''
숲에 막히지 않고 연결된 구간의 수 출력
'''

from collections import deque

N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

def bfs(x, y):

    q = deque([(x, y)])
    visited[x][y] = True

    while q:

        i, j = q.popleft()

        for di, dj in dir:
            ni, nj = (i + di) % N, (j + dj) % M

            if not visited[ni][nj] and not mp[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj))

for i in range(N):
    for j in range(M):
        if not visited[i][j] and not mp[i][j]:
            bfs(i, j)
            answer += 1

print(answer)