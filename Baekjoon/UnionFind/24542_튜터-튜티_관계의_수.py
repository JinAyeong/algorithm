
# size 기반 유니온 파인드
# python 42728 KB, 368 ms

import sys
input = sys.stdin.readline

# 경로 압축을 적용한 find 함수
def find(x):
    if parent[x] != x:               # 루트 노드가 아니라면
        parent[x] = find(parent[x])  # 루트 노드 찾으면서 경로 압축
    return parent[x]                 # 루트 노드 반환

# 유니온 연산 시, size를 업데이트하여 트리 크기 관리
def union(x, y):
    rootX = find(x) # x의 루트 노드 찾기
    rootY = find(y) # y의 루트 노드 찾기

    # 서로의 루트 노드가 다르면 (다른 집합이면) 연결해주기
    if rootX != rootY:
        if size[rootX] < size[rootY]:   # 트리의 높이가 더 작은 쪽(rootX)을 큰 쪽(rootY)에 붙임
            parent[rootX] = rootY
            size[rootY] += size[rootX]  # 합쳐진 집합의 크기 합치기
        else:                           # 트리의 높이가 같으면
            parent[rootY] = rootX       # 아무거나 루트 노드 갱신
            size[rootX] += size[rootY]  # 갱신한 루트 쪽으로 집합의 크기 합치기

# 입력 처리
N, M = map(int, input().split())

# 초기화
parent = [i for i in range(N)]  # 각 노드는 처음에 자기 자신이 루트
size = [1] * N  # 각 노드가 속한 집합의 크기 (초기에는 자기 자신만 있으므로 1)

# 유니온 파인드 적용
for _ in range(M):
    m1, m2 = map(int, input().split())
    union(m1-1, m2-1)

# 각 집합의 크기 계산
result = 1

for i in range(N):
    if parent[i] == i:
        result = (result * size[i]) % 1000000007

print(result)


#========================================================================================
# size, rank 기반 유니온 파인드
# python 83768 KB, 548 ms

import sys
input = sys.stdin.readline

# 경로 압축을 적용한 find 함수
def find(x):
    if parent[x] != x:               # 루트 노드가 아니라면
        parent[x] = find(parent[x])  # 루트 노드 찾으면서 경로 압축
    return parent[x]                 # 루트 노드 반환

# 유니온 연산 시, size를 업데이트하여 트리 크기 관리
def union(x, y):
    rootX = find(x) # x의 루트 노드 찾기
    rootY = find(y) # y의 루트 노드 찾기

    # 서로의 루트 노드가 다르면 (다른 집합이면) 연결해주기
    if rootX != rootY:
        if rank[rootX] < rank[rootY]:   # 트리의 높이가 더 작은 쪽(rootX)을 큰 쪽(rootY)에 붙임
            parent[rootX] = rootY
            size[rootY] += size[rootX]  # 합쳐진 집합의 크기 합치기
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
            size[rootX] += size[rootY]
        else:                           # 트리의 높이가 같으면
            parent[rootY] = rootX       # 아무거나 루트 노드 갱신
            size[rootX] += size[rootY]  # 갱신한 루트 쪽으로 집합의 크기 합치기
            rank[rootX] += 1            # 갱신한 루트 쪽으로 트리 높이 추가

# 입력 처리
N, M = map(int, input().split())
relationship = [list(map(int, input().split())) for _ in range(M)]

# 초기화
parent = [i for i in range(N)]  # 각 노드는 처음에 자기 자신이 루트
rank = [1] * N  # 각 토드가 속한 트리의 높이 (초기에는 1)
size = [1] * N  # 각 노드가 속한 집합의 크기 (초기에는 자기 자신만 있으므로 1)

# 유니온 파인드 적용
for m1, m2 in relationship:
    union(m1-1, m2-1)

# 각 집합의 크기 계산
result = 1
seen = set()

for i in range(N):
    root = find(i)        # i번 노드의 최상위 루트 찾기
    if root not in seen:  # 처음보는 집합이 나오면
        seen.add(root)    # 루트 기록 후 결과 값 갱신
        result = (result * size[root]) % 1000000007

print(result)