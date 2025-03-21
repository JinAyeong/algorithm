import sys
input = sys.stdin.readline

from collections import deque

K = int(input())

for _ in range(K):
    V, E = map(int, input().split()) # 정점 수, 간선 수
    adjl = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        adjl[v].append(u)
        adjl[u].append(v)

    visited = [0] * (V+1)

    def is_bipartite(n, num):

        q = deque([n])
        visited[n] = 1

        while q:
            cur = q.popleft()

            for next in adjl[cur]:
                if not visited[next]:
                    visited[next] = (1 if visited[cur] == 2 else 2)
                    q.append(next)
                else:
                    if visited[next] == visited[cur]:
                        return False

        return True

    result = 'YES'

    for i in range(1, V+1):
        if not visited[i]:
            if not is_bipartite(i, 1):
                result = 'NO'
                break

    print(result)