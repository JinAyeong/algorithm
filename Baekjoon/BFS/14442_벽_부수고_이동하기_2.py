'''
0: 이동 가능, 1: 이동 불가능
(N, M)까지 최단경로로 이동
벽 K개까지 부수고 이동 가능

벽 부순 유무 포함하여 저장
'''

import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())
mp = [list(input()) for _ in range(N)]

def solve():
    visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    q = deque([(0, 0, 0, 1)]) # (i, j), k, t

    while q:
        ci, cj, ck, ct = q.popleft()

        # 도착
        if (ci, cj) == (N-1, M-1):
            return ct

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj

            if not (0 <= ni < N and 0 <= nj < M):
                continue

            # 이동가능한 빈 칸일 경우
            if mp[ni][nj] == '0' and not visited[ni][nj][ck]:
                visited[ni][nj][ck] = ct + 1
                q.append((ni, nj, ck, ct + 1))

            # 벽 부숴야하는 경우
            elif mp[ni][nj] == '1' and ck + 1 <= K and not visited[ni][nj][ck + 1]:
                visited[ni][nj][ck + 1] = ct + 1
                q.append((ni, nj, ck + 1, ct + 1))

    return -1

print(solve())