'''
[설명]
8*8 체스판에서 탈출 : (7, 0) -> (0, 7)로 이동
1. 욱제의 이동 : 상하좌우 대각선으로 8방향 이동 또는 서있기
2. 움직이는 벽 : 모든 벽은 아래에 있는 행으로 한 칸씩 이동
2-1. 벽이 캐릭터가 있는 칸으로 이동하면 캐릭터 더이상 이동 불가능

[풀이]
'''

from copy import deepcopy
from collections import deque

mp = deque(list(input()) for _ in range(8))
dir = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
visited = [[False] * 8 for _ in range(8) for _ in range(64)]

# 매초마다 벽의 위치
mps = [deepcopy(mp)]
new_wall = deepcopy(deque(mp))

for i in range(8):
    new_wall.pop()
    new_wall.appendleft(['.'] * 8)
    mps.append(deepcopy(new_wall))

q = deque([(7, 0, 0)])
visited[0][7][0] = True

while q:
    i, j, t = q.popleft()

    # 가만히 있기
    q.append((i, j, t+1))

    # 움직이기
    for di, dj in dir:
        ni, nj = i + di, j + dj

        if 0 <= ni < 8 and 0 <= nj < 8 and not visited[t][ni][nj] and mps[t][ni][nj] == '.':
            q.append((ni, nj, t+1))