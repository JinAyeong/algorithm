N = int(input())
M = int(input())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])

parent = [i for i in range(N+1)]
rank = [1] * (N+1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

cost = 0
cnt = 0

for s, e, c in edges:
    if find(s) != find(e):
        union(s, e)
        cost += c
        cnt += 1
    if cnt == N-1:
        break

print(cost)