# 인접칸만 확인하며 삭제
# python 32544 KB 120 ms

N, M, T = map(int, input().split())
circles = [list(map(int, input().split())) for _ in range(N)]

def turn(x, d, k):  # x의 배수인 원판을 d(0: 시계, 1: 반시계) 방향으로 k칸 회전
    for i in range(x, N+1, x):
        if d == 0:  # 시계 방향
            circles[i-1] = circles[i-1][-k:] + circles[i-1][:-k]
        else:  # 반시계 방향
            circles[i-1] = circles[i-1][k:] + circles[i-1][:k]

def number_delete():
    deleted = False
    to_delete = set()

    for i in range(N):
        for j in range(M):
            if circles[i][j] == 0:
                continue

            num = circles[i][j]
            for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, (j + dj) % M

                if 0 <= ni < N and circles[ni][nj] == num:
                    to_delete.add((i, j))
                    to_delete.add((ni, nj))

    if to_delete:
        deleted = True
        for i, j in to_delete:
            circles[i][j] = 0

    return deleted


def number_control():
    total = sum(sum(circles[i]) for i in range(N))
    cnt = sum(1 for i in range(N) for j in range(M) if circles[i][j] > 0)

    if cnt == 0:
        return

    average = total / cnt  # 0을 제외한 평균값

    for i in range(N):
        for j in range(M):
            if circles[i][j] > 0:
                if circles[i][j] > average:
                    circles[i][j] -= 1
                elif circles[i][j] < average:
                    circles[i][j] += 1

for _ in range(T):

    # 1. 원판 회전
    x, d, k = map(int, input().split())
    turn(x, d, k)

    # 2-1. 인접하면서 같은 수가 있는 경우에 그 수 삭제
    if number_delete():
        continue

    # 2-2. 인접하면서 같은 수가 없는 경우에 원판 수의 합보다 작은 수는 += 1 큰 수는 -= 1
    number_control()

print(sum(sum(line) for line in circles))


#----------------------------------------------------------------------------
# bfs로 인접하고 같은 숫자 삭제
# python 35092 KB 176 ms

from collections import deque

N, M, T = map(int, input().split())
circles = [list(map(int, input().split())) for _ in range(N)]

def turn(x, d, k):  # x의 배수인 원판을 d(0: 시계, 1: 반시계) 방향으로 k칸 회전
    for i in range(x, N+1, x):
        if d == 0:  # 시계 방향
            circles[i-1] = circles[i-1][-k:] + circles[i-1][:-k]
        else:  # 반시계 방향
            circles[i-1] = circles[i-1][k:] + circles[i-1][:k]

def number_delete():

    deleted = False
    visited = [[False] * M for _ in range(N)]

    q = deque([])

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and circles[i][j] != 0:
                visited[i][j] = True
                q.append((circles[i][j], i, j))
                while q:
                    num, ci, cj = q.popleft()

                    for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        ni, nj = ci + di, cj + dj

                        if not (0 <= nj < M):
                            nj = (M-1 if nj < 0 else 0 if nj > M-1 else nj)

                        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and circles[ni][nj] == num:
                            deleted = True
                            visited[ni][nj] = True
                            circles[i][j] = 0
                            circles[ni][nj] = 0
                            q.append((num, ni, nj))

    return deleted


def number_control():
    total = sum(sum(circles[i]) for i in range(N))
    cnt = sum(1 for i in range(N) for j in range(M) if circles[i][j] > 0)

    if cnt == 0:
        return

    average = total / cnt  # 0을 제외한 평균값

    for i in range(N):
        for j in range(M):
            if circles[i][j] > 0:
                if circles[i][j] > average:
                    circles[i][j] -= 1
                elif circles[i][j] < average:
                    circles[i][j] += 1

for _ in range(T):

    # 1. 원판 회전
    x, d, k = map(int, input().split())
    turn(x, d, k)

    # 2-1. 인접하면서 같은 수가 있는 경우에 그 수 삭제
    if number_delete():
        continue

    # 2-2. 인접하면서 같은 수가 없는 경우에 원판 수의 합보다 작은 수는 += 1 큰 수는 -= 1
    number_control()

print(sum(sum(line) for line in circles))


#---------------------------------------------
# deque의 rorate 메서드 사용으로 원판 회전 시키기
# (초기 원판 배열을 deque으로 받아야 함)

def turn(x, d, k):  # x의 배수인 원판을 d(0: 시계, 1: 반시계) 방향으로 k칸 회전
    for i in range(x, N+1, x):
        if d == 0:  # 시계 방향
            circles[i-1].rotate(k)
        else:  # 반시계 방향
            circles[i-1].rotate(-k)