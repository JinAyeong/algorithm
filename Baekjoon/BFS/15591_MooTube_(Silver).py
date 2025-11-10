import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())
adjl = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, q, r = map(int, input().split())
    adjl[p].append((q, r))
    adjl[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())
    visited = [False] * (N+1)
    visited[v] = True

    q = deque([v])
    cnt = 0

    while q:
        cur = q.popleft()

        for next, usado in adjl[cur]:
            if not visited[next] and usado >= k:
                visited[next] = True
                cnt += 1
                q.append(next)
                
    print(cnt)
