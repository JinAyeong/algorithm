from collections import deque

N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

clouds = deque([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])

def move(d, s):

    watered = set()

    # 구름 이동
    while clouds:
        ci, cj = clouds.popleft()
        ni, nj = (ci + directions[d][0] * s) % N, (cj + directions[d][1] * s) % N
        mp[ni][nj] += 1
        watered.add((ni, nj))

    # 물복사 버그
    for wi, wj in watered:
        for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            ni, nj = wi + di, wj + dj
            if 0 <= ni < N and 0 <= nj < N and mp[ni][nj] > 0:
                mp[wi][wj] += 1

    # 새로운 구름 생성 (2 이상이면서 방금 물 내린 곳 제외)
    for i in range(N):
        for j in range(N):
            if mp[i][j] >= 2 and (i, j) not in watered:
                clouds.append((i, j))
                mp[i][j] -= 2


for _ in range(M):
    d, s = map(int, input().split())
    move(d-1, s)

result = sum(map(sum, mp))
print(result)