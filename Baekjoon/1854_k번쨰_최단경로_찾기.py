from heapq import heappush, heappop

n, m, k = map(int, input().split()) # 도시 수, 경로 수, k
adjl = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    adjl[a].append((c, b))
    adjl[b].append((c, a))

def dijkstra(end):

    heap_k = [] # 경로, 노드
    heap = [(0, 1)]
    dist = [float('inf')] * (n+1)
    dist[1] = 0

    while heap:

        cur_d, cur_n = heappop(heap)

        for d, next in adjl[cur_n]:



# n, m, k = map(int, input().split())
# dist = [[[float('inf')] for _ in range(k+1)] for _ in range(n+1) for _ in range(n+1)]
# for i in range(n):
#     dist[i][i][1] = 0
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     dist[a][b][1] = c
#     dist[b][a][1] = c
#
# def dijkstra(s, e, k):
#
#     heap = [()]