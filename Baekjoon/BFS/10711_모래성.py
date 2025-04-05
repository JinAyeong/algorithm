'''
자기 격자 주변 8방의 모래가 없는 부분의 수 >= 자기 모래성의 튼튼함 : 무너짐
1. 모래성 없는 부분 blank에 저장
2. blank 방문처리 하면서 순회 -> 주변 모래성 있는 부분 체크
3. 모래 다 무너진 곳 new_blank에 새로 저장 -> 1부터 다시 반복
'''

# 모래성 없는 부분 탐색

import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())
mp = [list(input()) for _ in range(H)]
dir = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
blank = deque()
cnt = 0

# 초기 모래성 없는곳 저장
for i in range(H):
    for j in range(W):
        if mp[i][j] == '.':
            blank.append((i, j))
        else:
            mp[i][j] = int(mp[i][j])

# 파도 반복
while True:
    new_blank = deque()

    while blank:
        ci, cj = blank.popleft()

        for di, dj in dir:
            ni, nj = ci + di, cj + dj

            if 0 <= ni < H and 0 <= nj < W and mp[ni][nj] != '.':
                mp[ni][nj] -= 1

                if mp[ni][nj] <= 0:
                    mp[ni][nj] = '.'
                    new_blank.append((ni, nj))

    if not new_blank:
        break

    blank = new_blank
    cnt += 1

print(cnt)


#----------------------------------------------------------
# 모래성 부분 탐색 : 메모리 초과
'''
자기 격자 주변 8방의 모래가 없는 부분의 수 >= 자기 모래성의 튼튼함 : 무너짐
1. 모래성 있는 부분 배열에 저장
2. 파도 한 번 칠때마다 저장된 모래래성 순회하며 새로운 배열에 다시 저장 후 새로운 배열 return
'''

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
mp = [list(input()) for _ in range(H)]
dir = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
sand = set()

# 파도 치기
def surf(arr):
    new_blank = []
    new_arr = set()

    for ci, cj, cs in list(arr):
        blank = 0

        for di, dj in dir:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < H and 0 <= nj < W and mp[ni][nj] == '.':
                blank += 1

        if blank >= cs:
            new_blank.append((ci, cj))

        else:
            new_arr.add((ci, cj, cs))

    for x, y in new_blank:
        mp[x][y] = '.'

    return new_arr

# 초기 파도 저장
for i in range(H):
    for j in range(W):
        if mp[i][j] != '.':
            sand.add((i, j, int(mp[i][j])))

cnt = 0

# 파도 반복
while True:
    new_sand = surf(sand)
    if sand == new_sand:
        break
    sand = new_sand
    cnt += 1

print(cnt)