'''
조건)
0 : 이동 가능, 1 : 이동 불가능 (벽)
- 벽을 부수고 이동할 수 있는 곳으로 변경
- 그 위치에서 이동할 수 있는 칸의 개수 세기

풀이)
방법 1. 각각의 칸마다 bfs 실행 -> 시간초과 O((N * M) * (N * M)) = O((N*M)^2)
방법 2. 처음에 한번의 bfs 전체 순회하며 각 칸의 크기 측정 ->
'''

from collections import deque

N, M = map(int, input().split())
mp = [list(input()) for _ in range(N)]
group_mp = [[-1] * M for _ in range(N)]
group_size = []

# 그룹화 함수
def bfs(i, j, id):

    q = deque([(i, j)])
    group_mp[i][j] = id
    size = 1

    while q:
        ci, cj = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < M and group_mp[ni][nj] == -1 and mp[ni][nj] == '0':
                group_mp[ni][nj] = id
                q.append((ni, nj))
                size += 1

    return size


# 벽 주변 방의 크기 구하는 함수
def break_wall(i, j):
    cur_size = 1
    seen = set()

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj

        if 0 <= ni < N and 0 <= nj < M and mp[ni][nj] == '0':
            group_id = group_mp[ni][nj]
            if group_id not in seen:
                seen.add(group_id)
                cur_size += group_size[group_id]

    return cur_size


# 1. 각각의 연결된 빈공간 그룹화
group_id = 0
for i in range(N):
    for j in range(M):
        if mp[i][j] == '0' and group_mp[i][j] == -1:
            group_size.append(bfs(i, j, group_id))
            group_id += 1


# 2. 각각의 벽 뚫었을때 상하좌루 그룹 탐색 후 크기 합치기
result = [['0'] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if mp[i][j] == '1':
            result[i][j] = str(break_wall(i, j) % 10)

for line in result:
    print("".join(line))