'''
N개의 집, M개의 길
마을을 두개로 분리
각 분리된 마을의 집을 연결하는 길은 최소로 유지
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = [i for i in range(N + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)

    # 연결되어있지 않으면 연결하고 True 반환
    if rootA != rootB:
        parent[rootB] = rootA
        return True

    # 연결되어있으면 False 반환
    return False

total_cost = 0
max_edge = 0
count = 0

for cost, a, b in edges:

    # 연결되어있지 않아서 연결했을경우, cost 추가하고 간선 최댓값 갱신
    if union(a, b):
        total_cost += cost
        max_edge = max(max_edge, cost)
        count += 1

        # N-1개 연결했으면 모든 마을 연결 완료
        if count == N - 1:
            break

# 전체 마을 연결 간선 중, 가장 비용이 많이 드는 간선 제거 -> 최솟값으로 마을 두개 만들기 가능
print(total_cost - max_edge)
