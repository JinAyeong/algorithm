'''
N개의 지점 사이에 M개의 도로와 W개의 웜홀
'''

def solve(N, M, W):
    edge = []

    for _ in range(M):
        s, e, t = map(int, input().split())
        edge.append((s, e, t))
        edge.append((e, s, t))

    for _ in range(W):
        s, e, t = map(int, input().split())
        edge.append((s, e, -t))

    dist = [0] * (N+1)

    for i in range(N):
        for s, e, t in edge:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == N-1:
                    return 'YES'
    return 'NO'


tc = int(input())
for _ in range(tc):
    N, M, W = map(int, input().split())
    print(solve(N, M, W))
