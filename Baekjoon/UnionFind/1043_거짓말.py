N, M = map(int, input().split())  # 사람들 수, 파티의 수
T, *T_lst = list(map(int, input().split()))  # 진실을 아는 사람수, 진실을 아는 사람 번호

parent = [i for i in range(N)]
rank = [1] * (N)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:
        if rank[rootX] < rank[rootY]: # 높이가 작은 트리를 더 큰 트리에 붙이기
            rank[rootY] += rank[rootX]
            parent[rootX] = rootY
        else:
            rank[rootX] += rank[rootY]
            parent[rootY] = rootX

parties = [] # 파티 리스트

for _ in range(M):
    P, *P_lst = list(map(int, input().split()))  # 이번 파티의 인원수, 이번 파티에 참여하는 사람 번호
    parties.append(P_lst)

    # 파티에 온 사람들 그룹화
    for p in range(P):
        union(P_lst[p-1]-1, P_lst[p]-1)

T_parent = set(find(t-1) for t in T_lst) # 진실을 아는사람들의 루트 노드

result = 0

# 파티 하나씩 보면서 거짓말할 수 있는지 없는지 체크
for party in parties:
    P_parent = set(find(p-1) for p in party)  # 해당 파티에 온사람들의 루트 노드

    # 이번 파티에 온 사람들의 루트 노드와 진실을 아는사람들의 루트 노드가 겹치는지 안겹치는지 확인
    if all(root not in T_parent for root in P_parent):
        result += 1

print(result)