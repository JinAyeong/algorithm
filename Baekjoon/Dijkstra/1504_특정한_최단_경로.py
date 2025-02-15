from heapq import heappush, heappop

N, E = map(int, input().split()) # 정점 수, 간선 수
adjl = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adjl[a].append((b, c))
    adjl[b].append((a, c))

stop1, stop2 = map(int, input().split())

# start 부터 end까지의 최단거리
def dijkstra(start, end):

    heap = [(0, start)]
    visited = [float('inf')] * (N+1)
    visited[start] = 0

    while heap:

        t, c = heappop(heap)

        if c == end:
            return t

        if visited[c] < t:
            continue

        for nc, nt in adjl[c]:
            if nt + t < visited[nc]:
                visited[nc] = nt + t
                heappush(heap, (nt+t, nc))

    return float('inf')

# 1 -> stop1 -> stop2 -> N
# 1 -> stop2 -> stop1 -> N 중 더 빠른거리 채택
case1 = dijkstra(1, stop1) + dijkstra(stop1, stop2) + dijkstra(stop2, N)
case2 = dijkstra(1, stop2) + dijkstra(stop2, stop1) + dijkstra(stop1, N)

result = min(case1, case2)

print(result if result != float('inf') else -1)