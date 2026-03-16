'''
미로 밖으로 나갈 수 있는 칸의 수 찾기
'''

from collections import deque
N, M = map(int, input().split())
mp = [input() for _ in range(N)]

dir = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
escaped = [[False] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def bfs(i, j):

    q = deque([(i, j)])
    cur_visited = {(i, j)}
    visited[i][j] = True
    can_escape = False

    while q:
        ci, cj = q.popleft()
        cur_d = mp[ci][cj]

        ni, nj = ci + dir[cur_d][0], cj + dir[cur_d][1]

        if 0 <= ni < N and 0 <= nj < M:

            if not visited[ni][nj]:
                q.append((ni, nj))
                cur_visited.add((ni, nj))
                visited[ni][nj] = True

            elif escaped[ni][nj]:
                can_escape = True

        else:
            can_escape = True

    if can_escape:
        for vi, vj in cur_visited:
            escaped[vi][vj] = True
        return len(cur_visited)
    
    return 0

answer = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            answer += bfs(i, j)

print(answer)