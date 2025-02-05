def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:
        if len(size[rootX]) < len(size[rootY]):
            parent[rootX] = rootY
            size[rootY] |= size[rootX]  # 합집합 연산
        else:
            parent[rootY] = rootX
            size[rootX] |= size[rootY]

N = int(input())
M = int(input())

parent = [i for i in range(N)]
size = [{i} for i in range(N)]

route = [list(map(int, input().split())) for _ in range(N)]
city = list(map(lambda x: int(x)-1, input().split()))

for a in range(N):
    for b in range(N):
        if route[a][b] == 1:
            union(a, b)

p = parent[city[0]]

# 모든 여행지의 부모가 같으면 YES, 아니면 NO
for c in city:
    if parent[c] != p:
        print('NO')
        exit(0)

print('YES')