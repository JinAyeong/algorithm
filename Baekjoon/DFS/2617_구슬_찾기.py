N, M = map(int, input().split())
low = [[] for _ in range(N+1)] # weight[n] : n번 구슬보다 가벼운 구슬
high = [[] for _ in range(N+1)] # weight[n] : n번 구슬보다 무거운 구슬

for _ in range(M):
    g1, g2 = map(int, input().split())
    low[g1].append(g2)
    high[g2].append(g1)

def dfs(n, weight):

    if weight == 'low':
        lst = low[n]

    else:
        lst = high[n]

    cnt = 0

    for next in lst:
        if not visited[next]:
            visited[next] = True
            cnt += 1 + dfs(next, weight)

    return cnt


answer = 0

for i in range(1, N+1):
    visited = [False] * (N+1)
    visited[i] = True

    if dfs(i, 'low') >= (N + 1) // 2 or dfs(i, 'high') >= (N + 1) // 2:
        answer += 1

print(answer)