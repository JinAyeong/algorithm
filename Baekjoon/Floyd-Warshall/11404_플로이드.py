# 플로이드-워셜
n = int(input())
m = int(input())
dist= [[float('inf')] * n for _ in range(n)]

for x in range(n):
    dist[x][x] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for x in range(n):
    for y in range(n):
        if dist[x][y] == float('inf'):
            dist[x][y] = 0

for line in dist:
    print(*line)