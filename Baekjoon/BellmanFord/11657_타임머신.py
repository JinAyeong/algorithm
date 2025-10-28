'''
A, B, C = 시작, 도착, 버스이동시간
'''

N, M = map(int, input().split())
dist = [float('inf')] * (N+1)
edge = [tuple(map(int, input().split())) for _ in range(M)]


def bellman_ford(start):
    dist[start] = 0
    
    for i in range(N):

        for j in range(M):
            cur, next, cost = edge[j]
            if dist[cur] != float('inf') and dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost

                if i == N-1:
                    return True

    return False

negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == float('inf'):
            print(-1)
        else:
            print(dist[i])