from collections import deque

N, M = map(int, input().split())
adjl = [[] for _ in range(N+1)]

def solve(s, e):

    q = deque([(s, 0)])
    visited = [False] * (N+1)
    visited[s] = True

    while q:
        cur, dist = q.popleft()

        if cur == e:
            return dist

        for next, weight in adjl[cur]:
            if not visited[next]:
                visited[next] = True
                q.append((next, dist + weight))


for _ in range(N-1):
    a, b, d = map(int, input().split())
    adjl[a].append((b, d))
    adjl[b].append((a, d))

for _ in range(M):
    s, e = map(int, input().split())
    print(solve(s, e))
