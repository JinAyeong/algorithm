'''
1. 낚시왕 오른쪽으로 한 칸 이동
2. 낚시왕이 있는 열에서 땅과 가장 가까운 상어 잡기
3. 상어 이동 (초마다 n칸 이동0, 범위 벗어날경우 방향 바꿔서 그대로 이동)
4. 한 칸에 두 마리 이상의 상어가 있을 경우, 크기가 큰 상어가 나머지 다 잡아먹음
'''

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

R, C, M = map(int, input().split())  # 세로, 가로, 상어 수
mp = [[[] for _ in range(C)] for _ in range(R)]
sharks = {}
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # 위, 아래, 오른쪽, 왼쪽

for i in range(M):
    r, c, s, d, z = map(int, input().split())  # 위치, 속력, 이동방향, 크기
    heappush(mp[r-1][c-1], (z, i))
    sharks[i] = [s, d-1, z]


def move():
    new_mp = [[[] for _ in range(C)] for _ in range(R)]

    for a in range(R):
        for b in range(C):

            # 해당 위치에 상어 없을 경우 continue
            if not mp[a][b]:
                continue

            _, ci = heappop(mp[a][b])  # 상어 크기(샤용안함), 상어 번호
            cs, cd, cz = sharks[ci]  # 해당상어번호(ci)의 속도, 방향, 크기

            na, nb = a, b  # 현재 상어 위치

            # 상어 최종 위치 계산

            if cd <= 1:  # 위, 아래 방향일 경우
                cycle = (R - 1) * 2  # 상어 이동 가능 범위 (사이클)
                na = (a + cs * direction[cd][0]) % cycle  # 상어 이동

                if na >= R:  # 범위 벗어났을 경우 조정
                    na = cycle - na
                    cd = 1 - cd

            else:  # 오른쪽, 왼쪽 방향일 경우
                cycle = (C - 1) * 2  # 상어 이동 가능 범위 (사이클)
                nb = (b + cs * direction[cd][1]) % cycle  # 상어 이동

                if nb >= C:  # 범위 벗어났을 경우 조정
                    nb = cycle - nb
                    cd = 5 - cd

            # 상어 이동 후, 새로운 위치 저장
            heappush(new_mp[na][nb], (cz, ci))
            sharks[ci] = [cs, cd, cz]

    return new_mp  # 새로운 상어 배열 리턴


def fight():
    for x in range(R):
        for y in range(C):

            # 해당 위치에 상어가 두마리 이상 있을 경우, 한마리 남을때까지 pop
            while len(mp[x][y]) > 1:
                _, ci = heappop(mp[x][y])  # 해당 위치에서 상어 제거
                sharks.pop(ci)  # 해당 번호의 상어 제거


def fishing(cur): # 낚시왕의 현재 위치 cur

    # 가장 가까운 행 탐색하며 상어 있으면 상어 크기 return
    for r in range(R):
        if mp[r][cur]:
            _, ci = heappop(mp[r][cur])
            size = sharks[ci][2]
            sharks.pop(ci)
            return size
    return 0

result = 0

for king in range(C):
    result += fishing(king)
    mp = move()
    fight()

print(result)
