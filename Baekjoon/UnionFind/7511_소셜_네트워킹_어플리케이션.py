import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    print(f'Scenario {t+1}:')
    n = int(input()) # 유저의 수
    k = int(input()) # 친구 관계 수

    parent = [i for i in range(n)]
    rank = [1] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)

        if rootX != rootY:
            if rank[rootX] < rank[rootY]:
                rank[rootY] += rank[rootX]
                parent[rootX] = rootY
            else:
                rank[rootX] += rank[rootY]
                parent[rootY] = rootX


    # 친구 관계 (a, b는 친구)
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)

    m = int(input()) # 미리 구할 쌍의 수

    # 구해야 하는 쌍의 수
    for _ in range(m):
        u, v = map(int, input().split())
        result = find(u) == find(v)
        print(1 if result else 0)

    if t != T-1:
        print()