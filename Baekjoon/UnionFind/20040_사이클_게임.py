# import sys
# input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n)]
size = [1] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):

    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:
        if size[rootX] <= size[rootY]:
            size[rootY] += size[rootX]
            parent[rootX] = rootY
        else:
            size[rootX] += size[rootY]
            parent[rootY] = rootX

found = False

for c in range(1, 1+m):
    a, b = map(int, input().split())

    if find(a) == find(b):
        print(c)
        found = True
        break

    union(a, b)

if not found:
    print(0)