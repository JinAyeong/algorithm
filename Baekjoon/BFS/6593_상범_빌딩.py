'''
# : 막힘
. : 비어있음
S : 시작
E : 출구
'''

from collections import deque

# 시작점 찾기
def start_find(L, R, C, mp):
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if mp[l][r][c] == 'S':
                    return (l, r, c)

while True:

    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break

    mp = []

    # 건물 만들기
    for i in range(L):
        mp.append([list(input()) for _ in range(R)])
        _ = input()

    # 시작점 찾기
    start = start_find(L, R, C, mp)

    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    visited[start[0]][start[1]][start[2]] = True
    q = deque([(0, start[0], start[1], start[2])])
    result = 'Trapped!'

    # bfs
    while q:
        cd, cl, cr, cc = q.popleft()

        if mp[cl][cr][cc] == 'E':
            result = f'Escaped in {cd} minute(s).'
            break

        for dl, dr, dc in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
            nl, nr, nc = cl + dl, cr + dr, cc + dc

            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C and not visited[nl][nr][nc] and mp[nl][nr][nc] != '#':
                visited[nl][nr][nc] = True
                q.append((cd + 1, nl, nr, nc))

    print(result)