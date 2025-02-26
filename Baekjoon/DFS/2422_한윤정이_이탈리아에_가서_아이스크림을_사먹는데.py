N, M = map(int, input().split())
can_ice = [[True] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    can_ice[a][b] = False
    can_ice[b][a] = False

result = 0

def dfs(i, start, select):
    global result

    if i == 3:
        a, b, c = select
        if can_ice[a][b] and can_ice[b][c] and can_ice[a][c]:
            result += 1
        return

    for j in range(start, N + 1):
        if j not in select:
            dfs(i + 1, j + 1, select + [j])

dfs(0, 1, [])
print(result)
