import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
size = [1] * (n+1)

# 집합 결합
def union(a, b):

    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        if size[rootA] < size[rootB]:
            parent[rootA] = rootB
            size[rootB] += size[rootA]
        else:
            parent[rootB] = rootA
            size[rootA] += size[rootB]

# 부모 찾기
def find(a):

    if parent[a] != a:
        parent[a] = find(parent[a])

    return parent[a]

for _ in range(m):
    order, a, b = map(int, input().split())

    if order == 0:
        union(a, b)

    elif order == 1:
        if find(a) == find(b):
            print('yes')
        else:
            print('no')