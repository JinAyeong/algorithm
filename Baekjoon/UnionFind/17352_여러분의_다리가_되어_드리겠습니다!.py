import sys
input = sys.stdin.readline

N = int(input())

def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        if size[rootA] <= size[rootB]:
            size[rootB] += size[rootA]
            parent[rootA] = rootB
        else:
            size[rootA] += size[rootB]
            parent[rootB] = rootA

def find(a):

    if parent[a] != a:
        parent[a] = find(parent[a])

    return parent[a]

parent = [i for i in range(N+1)]
size = [1] * (N+1)

for _ in range(N-2):
    x, y = map(int, input().split())
    union(x, y)

found = False

for i in range(1, 1+N):
    if found:
        break
    for j in range(1, 1+N):
        if find(i) != find(j):
            found = True
            print(i, j)
            break