'''
현재 위치에서 가장 가까운 손님에게 가기 (거리가 같을 경우 행번호 -> 열번호 순서로 탐색)
현재 택시와 같은 위치라면 거리 = 0
한칸 이동마다 연료 1 소모
목적지 도착시 승객 이동 중 소모한 연료의 두배 충전
이동중 연료 바닥나면 영업 종료 (도착과 동시에 연료 바닥날시에는 이동 성공)
'''

import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappush, heappop

N, M, fuel = map(int, input().split())
mp = [list(input().split()) for _ in range(N)]
R, C = map(int, input().split())
start = {}
end = []
for c in range(M):
    si, sj, ei, ej = map(int, input().split())
    start[(si - 1, sj - 1)] = c
    end.append((ei-1, ej-1))

def client(x, y):
    global fuel
    q = deque([(x, y, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    candidates = []

    while q:
        cx, cy, cd = q.popleft()
        if (cx, cy) in start:
           heappush(candidates, (cd, cx, cy))

        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < N and mp[nx][ny] != '1' and not visited[nx][ny] and cd + 1 <= fuel:
                visited[nx][ny] = True
                q.append((nx, ny, cd + 1))

    if not candidates:
        return -1, -1
    ld, lx, ly = heappop(candidates)
    fuel -= ld
    return lx, ly

def move(x, y, num):
    global fuel
    q = deque([(x, y, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True

    while q:
        cx, cy, cd = q.popleft()
        if end[num] == (cx, cy):
            fuel += cd
            return cx, cy

        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < N and mp[nx][ny] != '1' and not visited[nx][ny] and cd + 1 <= fuel:
                visited[nx][ny] = True
                q.append((nx, ny, cd + 1))

    return -1, -1

cnt = 0
cur_start = (R-1, C-1)
while cnt < M:
    r, c = client(cur_start[0], cur_start[1])
    if (r, c) == (-1, -1):
        print(-1)
        exit(0)

    idx = start.pop((r, c))

    nr, nc = move(r, c, idx)
    if (nr, nc) == (-1, -1):
        print(-1)
        exit(0)

    start[idx] = ""
    cnt += 1
    cur_start = (nr, nc)

print(fuel)