


#-------------------------------------------------------------------------
# dfs, 방문처리

import sys

sys.setrecursionlimit(10000000)

# (x,y) -> (r,c) 탈출
# 거리는 총 K, 중복 방문 가능
# l, r, u, d = 왼, 오, 위, 아 (사전순 제일 빠른 경로로 탈출) d l r u

def move(n, m, i, j, r, c, k, order):
    global answer, visited

    if answer != 'impossible':
        return

    direction = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    char = {0: 'd', 1: 'l', 2: 'r', 3: 'u'}

    if len(order) == k and (i, j) == (r, c):
        answer = order
        return

    if len(order) > k:
        return

    for d in range(4):
        ni, nj = i + direction[d][0], j + direction[d][1]

        if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 'z':
            visited[ni][nj] == order + char[d]
            move(n, m, ni, nj, r, c, k, order + char[d])


def solution(n, m, x, y, r, c, k):
    global answer, visited

    answer = 'impossible'

    if abs(r - x) + abs(c - y) > k:
        return answer

    visited = [['z'] * m for _ in range(n)]

    move(n, m, x - 1, y - 1, r - 1, c - 1, k, '')

    return answer