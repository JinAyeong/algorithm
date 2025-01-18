# dfs

N, M = map(int, input().split()) # 세로, 가로

fuel = [list(map(int, input().split())) for _ in range(N)]
min_fuel = float('inf')

def move(i, direction, j, cur_f):
    global min_fuel

    if i == N:
        min_fuel = min(min_fuel, cur_f)
        return

    if cur_f > min_fuel:
        return

    if direction != 'l':
        if 0 <= j+1 < M:
            move(i + 1, 'l', j + 1, cur_f + fuel[i][j + 1])

    if direction != 's':
        move(i + 1, 's', j, cur_f + fuel[i][j])

    if direction != 'r':
        if 0 <= j-1 < M:
            move(i + 1, 'r', j-1, cur_f + fuel[i][j-1])

for m in range(M):
    move(1, '', m, fuel[0][m])

print(min_fuel)