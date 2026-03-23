from collections import deque

N, M = map(int, input().split())
mp = [input() for _ in range(N)]

def find_doyeon():
    for i in range(N):
        for j in range(M):
            if mp[i][j] == 'I':
                return (i, j)
    return (0, 0)

doyeon = find_doyeon()

q = deque([doyeon])
visited = [[False] * M for _ in range(N)]
visited[doyeon[0]][doyeon[1]] = True
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = 0

while q:

    i, j = q.popleft()

    for di, dj in dir:
        ni, nj = i + di, j + dj

        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and (mp[ni][nj] != 'X'):
            if mp[ni][nj] == 'P':
                answer += 1
            q.append((ni, nj))
            visited[ni][nj] = True

print('TT' if answer == 0 else answer)