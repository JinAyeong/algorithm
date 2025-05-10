import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]

parent = [[(i, j) for j in range(M)] for i in range(N)]
size = [[1 for _ in range(M)] for _ in range(N)]
direction = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

# find 함수 (경로 압축)
def find(pos):
    x, y = pos
    if parent[x][y] != (x, y):
        parent[x][y] = find(parent[x][y])
    return parent[x][y]

# union 함수 (크기 기준 union)
def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        ax, ay = root_a
        bx, by = root_b
        if size[ax][ay] < size[bx][by]:
            parent[ax][ay] = root_b
            size[bx][by] += size[ax][ay]
        else:
            parent[bx][by] = root_a
            size[ax][ay] += size[bx][by]

# 방향대로 union 수행
for i in range(N):
    for j in range(M):
        dx, dy = direction[grid[i][j]]
        ni, nj = i + dx, j + dy
        union((i, j), (ni, nj))

# 유일한 루트의 개수 세기
unique_roots = set()
for i in range(N):
    for j in range(M):
        unique_roots.add(find((i, j)))

print(len(unique_roots))
