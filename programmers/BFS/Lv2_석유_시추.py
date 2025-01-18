from collections import deque

def dig(i, j, n, m, land):
    global oil, visited

    q = deque([(i, j)])

    visited_column = {j}
    cur_oil = 1

    while q:
        r, c = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + di, c + dj

            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and land[nr][nc]:
                visited_column.add(nc)
                q.append((nr, nc))
                visited[nr][nc] = True
                cur_oil += 1

    for v in list(visited_column):
        oil[v] += cur_oil


def solution(land):
    global oil, visited

    n = len(land)  # 세로
    m = len(land[0])  # 가로

    oil = [0] * m  # 각 열마다 파면 나오는 오일량

    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):

            if land[i][j] and not visited[i][j]:
                visited[i][j] = True
                dig(i, j, n, m, land)

    answer = max(oil)

    return answer


#------------------------------------------------------
# 시간초과

from collections import deque

def dig(i, n, m, land):
    oil = 0

    q = deque([])

    visited = [[False] * m for _ in range(n)]

    for d in range(n):

        if land[d][i]:
            visited[d][i] = True
            q.append((d, i))
            oil += 1

    while q:
        r, c = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + di, c + dj

            if 0 <= nr < n and 0 <= nc < m and land[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = True
                oil += 1
                q.append((nr, nc))

    return oil


def solution(land):
    answer = 0

    n = len(land)  # 세로
    m = len(land[0])  # 가로

    for i in range(m):
        answer = max(answer, dig(i, n, m, land))
        if answer == 250000:
            break

    return answer