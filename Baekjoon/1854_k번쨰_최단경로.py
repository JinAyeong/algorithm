n, m, k = map(int, input().split())
dist = [[[float('inf')] for _ in range(k+1)] for _ in range(n+1) for _ in range(n+1)]
for i in range(n):
    dist[i][i][1] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b][1] = c
    dist[b][a][1] = c

def dijkstra(s, e, k):

    heap = [()]