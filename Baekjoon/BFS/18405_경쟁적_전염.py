'''
- 번호가 낮은 바이러스 번허 증식
- 1초마다 상하좌우 방향으로 증식
- S초 후에 (X, Y)에 존재하는 바이러스의 종류 출력
'''

from collections import deque

N, K = map(int, input().split()) # 칸 수, 바이러스 최대 번호

mp = [list(map(int, input().split())) for _ in range(N)]

S, X, Y = map(int, input().split()) # S초 후에 (X, Y)칸 바이러스 번호 출력

q = []


for i in range(N):
    for j in range(N):
        if mp[i][j] != 0:
            q.append((mp[i][j], i, j))

q.sort()
q = deque(q)

def cycle(virus):

    new_virus = deque([])

    while virus:
        num, ci, cj = virus.popleft()

        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < N and mp[ni][nj] == 0:
                mp[ni][nj] = num
                new_virus.append((num, ni, nj))

    return new_virus

t = 0

while t < S and q:
    q = cycle(q)
    t += 1

    if t == S or not q:
        break

print(mp[X-1][Y-1])