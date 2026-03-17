'''
연구소는 크기가 N*N인 정사각형
0: 빈칸, 1: 벽, 2: 바이러스 놓을 수 있는 칸
바이러스를 모든 공간에 퍼트리는데 드는 최소 시간 출력, 불가능하면 -1
'''

from collections import deque

N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
virus_pos = []
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
blank_cnt = -M
answer = float('inf')

# 바이러스가 있는 칸 조회
for i in range(N):
    for j in range(N):
        if mp[i][j] == 2:
            virus_pos.append((i, j))

virus_pos_cnt = len(virus_pos)

# 1. 바이러스 선택
def dfs(n, idx, selected_virus):
    global answer

    if n == M:
        
        answer = min(bfs(selected_virus), answer)
        return
    
    for next in range(idx+1, virus_pos_cnt):
        dfs(n+1, next, selected_virus + [(virus_pos[next][0], virus_pos[next][1])])

# 2. 선택된 바이러스로 bfs
def bfs(selected_virus):
    max_t = 0

    q = deque(selected_virus)
    visited = [[-1] * N for _ in range(N)]

    # 바이러스 방문처리
    for i, j in selected_virus:
        visited[i][j] = 0

    # 탐색
    while q:
        i, j = q.popleft()
        t = visited[i][j]

        for di, dj in dir:
            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1 and mp[ni][nj] != 1:
                visited[ni][nj] = t + 1
                q.append((ni, nj))
                max_t = max(max_t, t+1)

    # 빈칸 다 채웠는지 확인
    for i in range(N):
        for j in range(N):
            if (mp[i][j] == 0 or mp[i][j] == 2) and visited[i][j] == -1:
                return float('inf')

    return max_t

dfs(0, -1, [])

print(answer if answer != float('inf') else -1)