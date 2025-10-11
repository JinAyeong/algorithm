def solution(n, s, a, b, fares):
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dist[i][i] = 0

    for x, y, f in fares:
        dist[x][y] = f
        dist[y][x] = f

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    answer = float('inf')
    for k in range(1, n + 1):
        answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])

    return answer