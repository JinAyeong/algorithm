n, m = map(int, input().split())  # 집하장 수, 경로 수
result = [['-'] * n for _ in range(n)]  # [i][j] : i에서 j로 갈 때 처음 방문해야하는 노드
dist = [[float('inf')] * n for _ in range(n)]

for _ in range(m):
    s, e, c = map(int, input().split())
    if dist[s-1][e-1] > c:
        dist[s-1][e-1] = c
        dist[e-1][s-1] = c
        result[s-1][e-1] = e
        result[e-1][s-1] = s

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                # i에서 j로 갈 때 처음 방문해야하는 노드 = i에서 k(경유지)로 갈 때 처음 방문해야하는 노드
                result[i][j] = result[i][k]

for line in result:
    print(*line)