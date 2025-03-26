N = int(input())
adjl = [list(map(int, input().split())) for _ in range(N)]
result = float('inf')
route = []

def dfs(i, expense):
    global result

    if i == N:
        next_expense = adjl[route[-1]][route[0]]
        if next_expense == 0:
            return
        total_expense = expense + next_expense
        result = min(total_expense, result)
        return

    if expense >= result:
        return

    for j in range(N):
        cur = route[-1]

        if j not in route:

            next_expense = adjl[cur][j]
            if next_expense == 0:
                continue

            route.append(j)
            dfs(i + 1, expense + next_expense)
            route.pop()

for i in range(N):
    route.append(i)
    dfs(1, 0)
    route.pop()

print(result)