'''

'''

N, Q = map(int, input().split())
adjl = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, q, r = map(int, input().split())
    adjl[p].append((q, r))
    adjl[q].append((p, r))

def dfs(cur, end, min_usado, visited):

    if cur == end:
        return min_usado
    
    for next, usado in adjl[cur]:
        if not visited[next]:
            visited[next] = True
            dfs(next, end, min(min_usado, usado))
            visited[next] = False

for _ in range(Q):
    k, v = map(int, input().split())

    cnt = 0

    for i in range(1, N+1):
        if i == v:
            continue
        visited = [False] * (N+1)
        visited[i] = True
        dfs(v, i, float('inf'), visited)
