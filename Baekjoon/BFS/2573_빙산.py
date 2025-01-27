# python 2048 ms, 35436 KB
# pypy 524 ms, 205212 KB
# 1. 빙산 다 녹을 때 까지 while
# 2. 처음 input에서 빙산인 부분만 따로 저장
# 3. 그 부분만 탐색하면서 빙산 녹이고 새로운 빙산 배열 return
# 4. 새로운 빙산 배열을 가지고 다시 빙산 덩어리 센 후 빙산 수 return
# 5. 덩어리 2개 이상 나올때, 아니면 다 녹았을 때 (0개) 일 때 결과 갱신하고 break

from collections import deque

N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
ice = []

for a in range(N):
    for b in range(M):
        if sea[a][b] != 0:
            ice.append((a, b))


def melt(arr):
    iced = [[False] * M for _ in range(N)]
    new_arr = []

    for i, j in arr:
        iced[i][j] = True
        m = 0

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < M and not iced[ni][nj] and sea[ni][nj] == 0:
                m += 1

        if m < sea[i][j]:
            sea[i][j] -= m
            new_arr.append((i, j))

        else:
            sea[i][j] = 0

    return new_arr

def ice_count(arr):
    cnt = 0
    visited = [[False] * M for _ in range(N)]

    for i, j in arr:
        if visited[i][j]:
            continue

        visited[i][j] = True
        cnt += 1

        q = deque([(i, j)])

        while q:
            ci, cj = q.popleft()

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = ci + di, cj + dj

                if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and sea[ni][nj] != 0:
                    visited[ni][nj] = True
                    q.append((ni, nj))

    return cnt

result = 0

while True:

    ice = melt(ice)
    result += 1

    cur_cnt = ice_count(ice)

    if cur_cnt >= 2:
        break

    elif cur_cnt == 0:
        result = 0
        break

print(result)


#------------------------------------------------------------
# python 시간초과
# pypy 1668 ms, 215748 KB
# 1. 빙산 다 녹을 때 까지 while
# 2. 전체 N * M 배열 탐색하면서 바닷물인 경우에 그 주위를 보면서 빙산이 있는 경우 빙산 -= 1 녹이기
# 3. 녹인 후 전체 배열 return
# 4. 전체 N * M 배열 탐색하면서 빙산 덩어리 세기
# 5. 다 센 후 덩어리 return
# 6. 덩어리 2개 이상 나올때, 아니면 다 녹았을 때 (0개) 일 때 결과 갱신하고 break


N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]

def melt(arr):
    iced = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and not iced[i][j]:

                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] > 0:
                        iced[ni][nj] = True
                        arr[ni][nj] -= 1

    return arr

def ice_count(arr):
    cnt = 0
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and not visited[i][j]:
                visited[i][j] = True
                q = deque([(i, j)])

                while q:
                    ci, cj = q.popleft()

                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = ci + di, cj + dj

                        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] != 0:
                            visited[ni][nj] = True
                            q.append((ni, nj))

                cnt += 1

    return cnt

result = 0
while True:

    ice = melt(ice)
    result += 1

    cur_cnt = ice_count(ice)

    if cur_cnt >= 2:
        break

    elif cur_cnt == 0:
        result = 0
        break

print(result)