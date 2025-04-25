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
visited = [[False] * M for _ in range(N)]
island = deque([])
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
bridge = []

# 섬 끝부분 찾기
def find_island(x, y, num):
    q = deque([(x, y)])
    visited[x][y] = True
    mp[x][y] = num

    while q:
        cx, cy = q.popleft()
        is_edge = False

        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if mp[nx][ny] == 1:
                        visited[nx][ny] = True
                        mp[nx][ny] = num
                        q.append((nx, ny))
                    elif mp[nx][ny] == 0:
                        is_edge = True
            else:
                is_edge = True

        if is_edge:
            island.append((cx, cy, num))


# 섬 끝부분에서 다른 섬으로 연결하기
def build(x, y, num, d):
    length = 0
    cx, cy = x, y

    while True:
        cx += direction[d][0]
        cy += direction[d][1]

        if not (0 <= cx < N and 0 <= cy < M):
            break

        if mp[cx][cy] == num:
            break

        if mp[cx][cy] != 0 and mp[cx][cy] != num:
            if length >= 2:
                bridge.append((length, num, mp[cx][cy]))
            break

        if mp[cx][cy] == 0:
            length += 1

# 섬 찾기
cnt = 2
for i in range(N):
    for j in range(M):
        if not visited[i][j] and mp[i][j]:
            visited[i][j] = True
            find_island(i, j, cnt)
            cnt += 1


# 섬 연결하기
for x, y, num in island:
    for d in range(4):
        build(x, y, num, d)

parent = [i for i in range(cnt)]

def find(a):

    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 다리 연결
bridge.sort()
result = 0
count = 0
for length, a, b in bridge:
    if find(a) != find(b):
        union(a, b)
        result += length
        count += 1

# 섬 연결 확인
roots = set()

for idx in range(2, cnt):
    roots.add(find(idx))

print(result if len(roots) == 1 else -1)