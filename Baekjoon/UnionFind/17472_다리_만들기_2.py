'''
다리 연결 방법
1. 다리의 방향은 가로 또는 세로로만 연결 가능하다
2. 방향이 가로인 다리는 다리의 양 끝이 가로방향으로 섬과 인접, 세로도 마찬가지
3. 다리의 길이는 2 이상
4. 다리 교차 가능
5. 모든 섬이 연결하는 다리 길이의 최솟값 구하기
풀이
1. 섬의 테두리부분 전부 저장
    섬인 부분 (1) bfs로 탐색하며
    a. 주변이 같은 섬일 경우 q에 추가
    b. 주면이 같은 섬이 아닐 경우 island에 추가 (섬 번호 cnt 부여)
2. 그 섬 테두리에서 하나씩 꺼내서 상하좌우 탐색
    a. 한 방향으로만 탐색하며다른 섬에 도착했을 경우 섬 후보에 append(length, num1, num2)
    b. 다른 섬에 도착하지 못하는 경우 break
3. 섬 후보 중에서 다리 선택
    a. 후보 길이순으로 정렬
    b. 다리 하나 꺼내서 시작과 끝 다리 연결 (union)
4. 다리 연결 후 하나로 이루어져 있는지 검사 (find)
'''
from collections import deque

N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

visited = [[False] * M for _ in range(N)]
island_edges = deque()  # 섬의 가장자리 좌표들 저장
bridges = []            # 가능한 다리 후보들 저장

# 1. 하나의 섬을 탐색하여 번호를 붙이고, 가장자리를 저장
def mark_island(x, y, island_id):
    q = deque([(x, y)])
    visited[x][y] = True
    mp[x][y] = island_id

    while q:
        cx, cy = q.popleft()

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    if mp[nx][ny] == 1:
                        visited[nx][ny] = True
                        mp[nx][ny] = island_id
                        q.append((nx, ny))
                    elif mp[nx][ny] == 0:
                        island_edges.append((cx, cy, island_id))

# 2. 한 방향으로만 다리를 건설하며 다른 섬에 도달할 수 있는지 확인
def build_bridge(x, y, island_id, direction_index):
    dx, dy = directions[direction_index]
    length = 0
    nx, ny = x + dx, y + dy

    while 0 <= nx < N and 0 <= ny < M:
        if mp[nx][ny] == island_id:  # 자기 섬 만나면 중단
            break
        if mp[nx][ny] != 0 and mp[nx][ny] != island_id:
            if length >= 2:
                bridges.append((length, island_id, mp[nx][ny]))
            break
        # 바다인 경우 계속 진행
        length += 1
        nx += dx
        ny += dy

# 3. 모든 섬을 탐색하면서 번호 부여 및 가장자리 수집
island_id = 2  # 섬 번호는 2부터 시작
for i in range(N):
    for j in range(M):
        if not visited[i][j] and mp[i][j] == 1:
            mark_island(i, j, island_id)
            island_id += 1

# 4. 각 가장자리에서 다리 건설 시도
for x, y, id in island_edges:
    for d in range(4):
        build_bridge(x, y, id, d)

# 5. 다리 연결확인 및 연결하기
parent = [i for i in range(island_id)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        if a_root < b_root:
            parent[b_root] = a_root
        else:
            parent[a_root] = b_root

# 6. 다리 연결
bridges.sort()
total_length = 0
connection_count = 0

for length, a, b in bridges:
    if find(a) != find(b):
        union(a, b)
        total_length += length
        connection_count += 1

# 7. 모든 섬이 연결되어 있는지 확인
roots = set(find(i) for i in range(2, island_id))
print(total_length if len(roots) == 1 else -1)