'''
0: 빈칸
1: 벽
2: 바이러스
- 바이러스중, M개의 바이러스를 활성으로 변경하여 모든 칸에 바이러스 퍼뜨리기
- 활성 바이러스가 비활성 바이러스가 있는 칸으로 이동 -> 활성으로 변경
'''
from collections import deque

N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
virus = []
selected_virus = []
blank_space = 0

for i in range(N):
    for j in range(N):
        if mp[i][j] == 2:
            virus.append((i, j))
        elif mp[i][j] == 0:
            blank_space += 1

def bfs():

    q = deque(selected_virus)
    visited = [[-1] * N for _ in range(N)]
    cnt = 0
    max_sec = 0

    for x, y in selected_virus:
        visited[x][y] = 0
        q.append((x, y))

    while q:
        ci, cj = q.popleft()
        
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1 and mp[ni][nj] != 1:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
                if mp[ni][nj] == 0:
                    cnt += 1
                    max_sec = visited[ni][nj]

    if cnt == blank_space:
        return max_sec
    return float('inf')

result = float('inf')

def choice(i, idx):
    global result

    if i == M:
        result = min(bfs(), result)
        return
    
    for j in range(idx+1, len(virus)):
        selected_virus.append((virus[j][0], virus[j][1]))
        choice(i+1, j)
        selected_virus.pop()

choice(0, -1)

print(result if result != float('inf') else -1)