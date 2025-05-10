import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mp = [list(input()) for _ in range(N)]

parent = [[(i, j) for j in range(M)] for i in range(N)]
rank = [[1 for j in range(M)] for i in range(N)]
direction = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}

def find(tup):

    if parent[tup[0]][tup[1]] != tup:
        parent[tup[0]][tup[1]] = find(parent[tup[0]][tup[1]])
    return parent[tup[0]][tup[1]]

def union(tup1, tup2):

    root1 = find(tup1)
    root2 = find(tup2)

    if root1 != root2:
        if rank[root1[0]][root1[1]] < rank[root2[0]][root2[1]]:
            parent[root1[0]][root1[1]] = root2
            rank[root2[0]][root2[1]] += rank[root1[0]][root1[1]]
        else:
            parent[root2[0]][root2[1]] = root1
            rank[root1[0]][root1[1]] += rank[root2[0]][root2[1]]

for i in range(N):
    for j in range(M):
        dir = direction[mp[i][j]]
        next = (i+dir[0], j+dir[1])
        union((i, j), next)

total_parent = set()

for i in range(N):
    for j in range(M):
        total_parent.add(find((i, j)))

print(len(total_parent))