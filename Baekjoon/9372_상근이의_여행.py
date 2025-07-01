T = int(input())

N, M = map(int, input().split())
adjl = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

# for i in range(1, N+1):
    