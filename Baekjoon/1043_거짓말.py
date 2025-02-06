N, M = map(int, input().split())  # 사람들 수, 파티의 수
T, *T_lst = list(map(int, input().split()))  # 진실을 아는 사람수, 진실을 아는 사람 번호

parent = [i for i in range(N)]
rank = [1] * N


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


for _ in range(M):
    P, *P_lst = list(map(int, input().split()))  # 이번 파티의 인원수, 이번 파티에 참여하는 사람 번호

    for p in range(P):
        union(P_lst[p-1]-1, P_lst[p]-1)

print(parent)
print(rank)