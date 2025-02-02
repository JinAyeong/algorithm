import sys
input = sys.stdin.readline
from heapq import heappop, heappush

V, E = map(int, input().split()) # 정점 수, 간선 수
K = int(input()) # 시작 정점 번호
adjl = [[] for _ in range(V+1)]
visited = [float('inf')] * (V+1)
visited[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split()) # u -> v 가중치 w
    adjl[u].append((w, v))

heap = [(0, K)]

while heap:

    cur_w, cur_n = heappop(heap)

    if cur_w > visited[cur_n]:
        continue

    for next_w, next_n in adjl[cur_n]:

        next = next_w + cur_w

        if visited[next_n] > next:
            heappush(heap, (next, next_n))
            visited[next_n] = next

for i in range(1, V+1):
    if visited[i] == float('inf'):
        print('INF')

    else:
        print(visited[i])